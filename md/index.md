# Project Home

Welcome to the project documentation site!

## File Structure

- `/.github/workflows/deploy.yml`: GitHub Actions workflow configuration.
- `/main.py`: FastAPI application.
- `/docker-compose.yml`: Docker Compose configuration.
- `/docker-compose.debug.yml`: Docker Compose configuration for debugging.
- `/requirements.txt`: Project dependencies.
- `/mkdocs.yml`: MkDocs configuration file.
- `/static/`: Directory for static files.
- `/site/`: Directory for MkDocs output.

## Routes

- `/distances`: Get distances between major Polish cities and Krakow/Gdansk.
- `/osm`: Serve static CV in HTML format.
- `/wiki`: Serve MkDocs generated documentation.

## About

This project demonstrates how to build and deploy a FastAPI application with GitHub Actions, Docker, and MkDocs. It includes an example of serving static files, converting Markdown to HTML and PDF, and calculating geodesic distances.

Refer to the [README.md](https://github.com/yourusername/yourrepository) for detailed instructions on running and developing the project.
