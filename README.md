SARO – Web Application Vulnerability Scanner
A Python-based tool designed to detect common web application vulnerabilities like Cross-Site Scripting (XSS), SQL Injection (SQLi), and Cross-Site Request Forgery (CSRF). The scanner integrates with a simple web interface (Flask) and follows the OWASP Top 10 guidelines.

Objective:

Build an automated scanner that:
Crawls a target web application.
Identifies input fields/forms.
Injects malicious payloads to test for vulnerabilities.
Uses regex and heuristic matching to detect exploits.
Logs each vulnerability found along with evidence and severity.
Presents results through a user-friendly web interface.
Generates a downloadable PDF report for documentation.

Tools & Technologies
 
| Technology      | Purpose                              |
| --------------- | ------------------------------------ |
| Python 3        | Main language                        |
| `requests`      | HTTP/HTTPS request handling          |
| `BeautifulSoup` | HTML parsing and form discovery      |
| `re` (regex)    | Matching SQL error patterns          |
| `Flask`         | Web interface for scanning & results |
| `reportlab`     | PDF generation of results            |
| OWASP Checklist | Security benchmark and validation    |

 Execution Guide
 
a. Crawl Inputs and URLs
Uses requests and BeautifulSoup to recursively crawl internal links.

Parses HTML to find <form> elements and their fields.

b. Inject Payloads
Predefined payloads for:

XSS: <script>alert(1)</script>, "><img src=x onerror=alert(1)>

SQLi: ' OR '1'='1, '; DROP TABLE users;--

c. Analyze Responses
Scans for reflected payloads (XSS) or SQL error messages (SQLi).

Uses regex patterns to match common SQLi database errors.

d. Flask UI for Control
Users input a target URL via web form.

Results are dynamically displayed after scan completion.

e. Evidence Logging
Displays each vulnerability with:

Type

Payload used

Field/form affected

Matched OWASP Top 10 category

web_vuln_scanner/
├── app.py              # Flask web app controller
├── scanner.py          # Core vulnerability scanning logic
├── crawler.py          # Internal link discovery
├── reporter.py         # PDF report generation
├── templates/
│   └── index.html      # Web interface (SARO UI)
├── requirements.txt    # List of dependencies
└── README.md           # Project report and documentation

Vulnerabilities Detected

| Vulnerability | Description                               | OWASP Top 10 |
| ------------- | ----------------------------------------- | ------------ |
| XSS           | Script injection into input fields        | A03:2021     |
| SQL Injection | SQL queries crafted to break DB integrity | A03:2021     |
| CSRF          | Missing CSRF token in forms               | A01:2021     |

 Deliverables
✅ Fully working Python-based scanner
✅ Crawling & form detection using BeautifulSoup
✅ XSS and SQLi injection testing
✅ CSRF token presence check
✅ Flask-based responsive web interface
✅ Color-coded scan results
✅ Downloadable PDF report
✅ OWASP Top 10 alignment in results
✅ Ready-to-run requirements.txt

# Step 1: Clone and setup
git clone https://github.com/yourusername/web_vuln_scanner.git
cd web_vuln_scanner
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Start the application
python app.py

# Step 4: Visit the web interface
http://127.0.0.1:5000

Scan Report for: https://testphp.vulnweb.com

✅ CSRF Token Found

XSS:
❌ None found

SQL Injection:
❌ None found

Errors:
None
This project is ideal for:

Cybersecurity internships

OWASP education

Final-year mini projects

Web app security practice
