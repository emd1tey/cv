# src/utils/cv_generator.py
from fpdf import FPDF
import markdown
import os
from fastapi import FastAPI

async def create_cv(app: FastAPI):
    # Define paths for markdown, HTML, and PDF files
    markdown_file_path = "src/md/cv.md"
    html_file_path = "static/cv/index.html"
    pdf_output_path = "static/cv/resume.pdf"

    # Check if the HTML and PDF files already exist
    if os.path.exists(html_file_path) and os.path.exists(pdf_output_path):
        return  # Skip the generation if files already exist

    # Read the markdown content
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        content = file.read()
        html_content = markdown.markdown(content)

    # Define the HTML template
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

    # Write the HTML content to the file
    with open(html_file_path, 'w') as f:
        f.write(html_template)

    # Create PDF from HTML content
    pdf = FPDF()
    pdf.add_page()
    pdf.write_html(html_content)
    pdf.output(pdf_output_path)
