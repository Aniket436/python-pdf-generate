from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, darkblue

def create_hypertension_pdf(file_name="Hypertension_Clinical_Notes.pdf"):
    # Create PDF
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Starting vertical position
    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(darkblue)
    c.drawString(50, y, "HYPERTENSION")

    # Subtitle
    y -= 30
    c.setFont("Helvetica", 12)
    c.setFillColor(black)
    c.drawString(50, y, "A concise clinical overview")

    # Horizontal line
    y -= 15
    c.line(50, y, width - 50, y)
    y -= 40

    # Section function (with page break)
    def section(title, text):
        nonlocal y

        # Page break logic
        if y < 80:
            c.showPage()
            y = height - 50

        # Section Title
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(darkblue)
        c.drawString(50, y, title)
        y -= 20

        # Section Text
        c.setFont("Helvetica", 11)
        c.setFillColor(black)

        for line in text.split("\n"):
            if y < 80:  # new page if needed
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 11)

            c.drawString(60, y, line)
            y -= 15

        y -= 10  # extra spacing

    # Content sections
    section(
        "Definition",
        "Hypertension is a chronic medical condition\n"
        "characterized by persistent elevation of\n"
        "systemic arterial blood pressure."
    )

    section(
        "Classification (Adults)",
        "• Normal: <120 / <80 mmHg\n"
        "• Elevated: 120–129 / <80 mmHg\n"
        "• Stage 1: 130–139 / 80–89 mmHg\n"
        "• Stage 2: ≥140 / ≥90 mmHg"
    )

    section(
        "Common Causes",
        "• Essential (Primary) hypertension\n"
        "• Renal parenchymal disease\n"
        "• Endocrine disorders\n"
        "• Drug-induced causes"
    )

    section(
        "Target Organ Damage",
        "• Heart – Left ventricular hypertrophy\n"
        "• Brain – Stroke\n"
        "• Kidney – Chronic kidney disease\n"
        "• Eye – Hypertensive retinopathy"
    )

    section(
        "Basic Management",
        "• Lifestyle modification\n"
        "• Salt restriction\n"
        "• Pharmacotherapy as per stage\n"
        "• Regular monitoring"
    )

    # Save PDF
    c.save()
    print("PDF Generated Successfully:", file_name)


# Run the function
create_hypertension_pdf()
