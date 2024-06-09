# src/utils/cv_generator.py
import logging
import os

import markdown
from fpdf import FPDF

logger = logging.getLogger(__name__)


async def create_cv():
    markdown_file_path = "src/md/cv.md"
    html_file_path = "static/cv/index.html"
    pdf_output_path = "static/cv/resume.pdf"

    if os.path.exists(html_file_path) and os.path.exists(pdf_output_path):
        logger.info("HTML and PDF files already exist. Skipping generation.")
        return

    try:
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

        with open(html_file_path, "w") as f:
            f.write(html_template)
        logger.info(f"HTML file created at: {html_file_path}")

        pdf = FPDF()
        pdf.add_page()
        pdf.write_html(html_content)
        pdf.output(pdf_output_path)
        logger.info(f"PDF file created at: {pdf_output_path}")

    except Exception as e:
        logger.error(f"Error generating CV: {e}")
        raise
