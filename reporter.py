from reportlab.pdfgen import canvas

def generate_pdf(results, filename="report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)
    y = 800

    c.drawString(50, y, f"Scan Report for {results['url']}")
    y -= 30

    c.drawString(50, y, f"CSRF Token Found: {'Yes ✅' if results['csrf'] else 'No ❌'}")
    y -= 30

    for cat in ["xss", "sqli"]:
        c.drawString(50, y, f"{cat.upper()} Issues:")
        y -= 20
        if results[cat]:
            for issue in results[cat]:
                c.drawString(70, y, f"- {issue}")
                y -= 20
        else:
            c.drawString(70, y, "None ✅")
            y -= 20

    if results["errors"]:
        c.drawString(50, y, "Errors:")
        y -= 20
        for err in results["errors"]:
            c.drawString(70, y, f"- {err}")
            y -= 20

    c.save()

