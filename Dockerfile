FROM python:3.11.3-bullseye

RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY ./ /app/

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi
