# src/main.py

import uvicorn
import argparse
import json

from src.config.settings import STATIC_DIR, EXPOSE_PORT, APP_NAME, SERVER_URL, SECRET_TOKEN
from src.config.configs import configure_opentelemetry, configure_logging, create_app
from src.utils.gendoc import list_files_recursive

logger = configure_logging()
trace_provider = configure_opentelemetry(APP_NAME, SERVER_URL, SECRET_TOKEN)
app = create_app()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the web server app or generate documentation.")
    parser.add_argument("--demonize", action="store_true", help="Start daemon.")
    args = parser.parse_args()


    if args.demonize:
        uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)
        logger.info(f"App up| NAME {APP_NAME} | PORT {EXPOSE_PORT}")
    else:
        json_str = json.dumps(list_files_recursive(STATIC_DIR), indent=2)
        logger.info("Logging JSON object:\n%s", json_str)
