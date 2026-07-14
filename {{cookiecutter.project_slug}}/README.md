# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Structure

- `{{ cookiecutter.package_name }}/` — FastAPI app source
- `tests/` — unit tests (pytest)
- `Dockerfile` — container image definition
- `azure-pipelines.yml` — SCA (pip-audit), SAST (bandit), Test, and Build & Push (ACR) stages

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
uvicorn {{ cookiecutter.package_name }}.main:app --reload --port {{ cookiecutter.app_port }}
```

## Run tests

```bash
pytest --cov={{ cookiecutter.package_name }}
```

## Build container locally

```bash
docker build -t {{ cookiecutter.project_slug }}:local .
docker run -p {{ cookiecutter.app_port }}:{{ cookiecutter.app_port }} {{ cookiecutter.project_slug }}:local
```

## Pipeline setup

Update `dockerRegistryServiceConnection` in `azure-pipelines.yml` to match the name of your
Azure DevOps service connection to `{{ cookiecutter.container_registry_login_server }}` (or your target ACR).
