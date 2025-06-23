from flask import Flask, render_template, request, send>
from crawler import crawl
from scanner import scan_url
from reporter import generate_pdf
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    urls = []
    if request.method == "POST":
        url = request.form.get("url")
        urls = list(crawl(url))
        urls.insert(0, url)  # include the main URL too
        results = []
        for u in urls:
            res = scan_url(u)
            results.append(res)
        generate_pdf({"url": url, "xss": sum((r["xss"] >
                      "sqli": sum((r["sqli"] for r in r>
                      "csrf": any(r["csrf"] for r in re>
                      "errors": sum((r["errors"] for r >
    return render_template("index.html", results=result>

@app.route("/download")
def download():
    return send_file("report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
