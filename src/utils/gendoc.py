import json
import logging
import os
import subprocess

import aiofiles
import markdown
from fastapi.openapi.docs import get_swagger_ui_html
from fpdf import FPDF

from src.config.settings import OUTPUT_PDF_PATH, STATIC_DIR

logger = logging.getLogger(__name__)


async def create_openapi(app):
    doc_dir = os.path.join(STATIC_DIR, "docs")
    os.makedirs(doc_dir, exist_ok=True)

    swagger_html = get_swagger_ui_html(
        openapi_url="openapi.json",
        title=app.title + " - Swagger UI",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css",
    ).body
    logger.info("Generating FastAPI documentation")

    api_json = json.dumps(app.openapi()).encode("utf-8")

    await write_content_to_file(os.path.join(doc_dir, "openapi.json"), api_json)
    await write_content_to_file(os.path.join(doc_dir, "index.html"), swagger_html)


async def list_files_recursive(directory):
    files = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
            logger.info("Found file: %s", file_path)
    return files

async def write_content_to_file(filename: str, content: bytes):
    try:
        async with aiofiles.open(filename, "wb") as file:
            await file.write(content)
        logger.info(f"Successfully written to file: {filename}")
    except Exception as e:
        logger.error(f"Error writing to file {filename}: {e}")


async def build_mkdocs():
    try:
        result = subprocess.run(
            ["mkdocs", "build"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        logger.info(f"mkdocs build successful: {result.stdout.decode('utf-8')}")
    except subprocess.CalledProcessError as e:
        logger.error(f"mkdocs build failed: {e.stderr.decode('utf-8')}")
        raise


async def create_cv():
    markdown_file_path = "src/md/cv.md"
    html_file_path = os.path.join(STATIC_DIR, "cv/index.html")
    pdf_output_path = os.path.join(STATIC_DIR, OUTPUT_PDF_PATH)
    logger.info(f"Generating CV: {pdf_output_path}")

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

        os.makedirs(os.path.dirname(html_file_path), exist_ok=True)
        with open(html_file_path, "w") as f:
            f.write(html_template)
        logger.info(f"HTML file created at: {html_file_path}")

        pdf = FPDF()
        pdf.add_page()
        pdf.write_html(html_content)
        pdf.output(pdf_output_path)
        if os.path.isfile(pdf_output_path):
            logger.info("File exist")
        logger.info(f"PDF file created at: {pdf_output_path}")

    except Exception as e:
        logger.error(f"Error generating CV: {e}")
        raise


async def create_doc(app):
    try:
        await create_openapi(app)
        await build_mkdocs()
        await create_cv()
    except Exception as e:
        logger.error(f"Error create_doc: {e}")
        raise
