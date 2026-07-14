FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY {{ cookiecutter.package_name }} ./{{ cookiecutter.package_name }}

EXPOSE {{ cookiecutter.app_port }}

CMD ["uvicorn", "{{ cookiecutter.package_name }}.main:app", "--host", "0.0.0.0", "--port", "{{ cookiecutter.app_port }}"]
