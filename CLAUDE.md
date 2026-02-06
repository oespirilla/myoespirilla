# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal portfolio website for Oscar Espirilla. A single-page Flask app deployed on Google App Engine Standard (Python 3.12).

- **URL**: https://oespirilla.appspot.com
- **GCP Project ID**: `oespirilla`
- **Repo**: github.com:oespirilla/myoespirilla.git (branch: master)

## Architecture

Flask (`main.py`) serves `index.html` via `send_file()`. Static assets are served by App Engine's static handler (`/static` → `static/`). Frontend uses Bootstrap 5.3.3 and Font Awesome 6.7.2 via CDN. Custom styles in `static/css/style.css`.

## Commands

```bash
# Setup
uv venv && uv pip install -r requirements.txt

# Run locally
.venv/bin/flask --app main run

# Deploy to App Engine
gcloud app deploy app.yaml --quiet

# View logs
gcloud app logs tail -s default
```

## Preferences

- Use **uv** (not pip) for package management
- Use **Homebrew** for tool installs
- No co-author lines in commit messages
