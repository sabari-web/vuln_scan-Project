import requests
from bs4 import BeautifulSoup
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureReq>

# Payloads
xss_payloads = ["<script>alert(1)</script>", "'\"><img >
sqli_payloads = ["'", "' OR '1'='1", "'; DROP TABLE use>
sql_errors = [
    r"you have an error in your sql syntax",
    r"unclosed quotation mark after the character strin>
    r"sql syntax.*?mysql",
    r"warning.*?mysql",
    r"mysql_fetch",
    r"syntax error",
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scan_url(url):
    results = {
        "url": url,
        "xss": [],
        "sqli": [],
        "csrf": {"found": False, "owasp": "A01:2021 – B>
        "errors": []
    }

    try:
        res = requests.get(url, headers=headers, timeou>
        soup = BeautifulSoup(res.text, "html.parser")
        forms = soup.find_all("form")

        # CSRF Token Detection
        csrf_found = False
        for form in forms:
            inputs = form.find_all("input")
            for inp in inputs:
                name_or_id = (inp.get("name", "") + inp>
                if "csrf" in name_or_id:
                    csrf_found = True
                    break
        results["csrf"]["found"] = csrf_found

          for form in forms:
            action = form.get("action")
            method = form.get("method", "get").lower()
            form_url = requests.compat.urljoin(url, act>

            inputs = form.find_all("input")
            input_names = [i.get("name") for i in input>

            data = {name: "test" for name in input_name>

            for payload in xss_payloads + sqli_payloads:
                for name in input_names:
                    test_data = data.copy()
                    test_data[name] = payload

                    try:
                        if method == "post":
                            r = requests.post(form_url,>
                        else:
                            r = requests.get(form_url, >
                        
                        body = r.text.lower()

                        # Detect reflected payloads (XS>
                        if payload.lower() in body and >
                            results["xss"].append({
                                "message": f"XSS detect>
                                "owasp": "A03:2021 – In>
                            })

                        # Detect SQLi error messages
                        if payload in sqli_payloads:
                            for pattern in sql_errors:
                                if re.search(pattern, b>
                                    results["sqli"].app>
                                        "message": f"SQ>
                                        "owasp": "A03:2>
                                    })
                    except requests.exceptions.RequestE>
                        results["errors"].append(f"Form>

    except requests.exceptions.RequestException as e:
        results["errors"].append(f"Network error: {str(>

    return results

