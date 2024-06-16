from tabulate import tabulate
from src.utils.gendoc import write_content_to_file
import os
import logging


logger = logging.getLogger(__name__)
md_dir = os.path.join("src/md", "cloud/")

def make_name_clickable(records):
    """
    Make the 'name' field in each record clickable by converting it to a Markdown link.

    Parameters:
    - records (list): List of DNS records.

    Returns:
    - list: List of modified records with clickable 'name' fields.
    """
    for record in records:
        url = f"http://{record['name']}"
        record['name'] = f"[{record['name']}]({url})"
    return records

async def dict_to_markdown_table(data):
    """
    Convert a dictionary to a markdown table.

    Parameters:
    - data (dict): The dictionary to convert.

    Returns:
    - str: The markdown table as a string.
    """
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    paths = []
    tables = {}
    for domain, records in data.items():
        clickable_records = make_name_clickable(records)
        tables[domain] = tabulate(clickable_records, "keys", tablefmt="github")
        logger.info(f"tables[{domain}] = {tables[domain]}")
        logger.info(f"records = {clickable_records}")


    # Saving each table as an HTML file
    for domain, table_html in tables.items():
        file_path = os.path.join(md_dir, f"{domain}.md")

        await write_content_to_file(file_path, table_html.encode('ascii'))
        paths.append(file_path)
        print(f"Created file: {file_path}")
    return paths
