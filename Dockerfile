FROM python:3.11-slim

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY ./ /app/

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi
