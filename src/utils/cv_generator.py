# src/utils/cv_generator.py
from fpdf import FPDF
import markdown
from fastapi import FastAPI

async def create_cv(app: FastAPI):
    markdown_file_path = "src/md/cv.md"

    with open(markdown_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        html_content = markdown.markdown(content)

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CV</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    with open('static/cv/index.html', 'w') as f:
        f.write(html_template)

    pdf = FPDF()
    pdf.add_page()
    pdf.write_html(html_content)
    pdf.output("static/cv/resume.pdf")

