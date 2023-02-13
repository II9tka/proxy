FROM python:3.10

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN apt update && apt install -y netcat
RUN python3 -m pip install poetry

RUN apt-get update && apt-get upgrade -y && apt-get -y install postgresql gcc python3-dev musl-dev

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir poetry

COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

RUN poetry install

COPY . /app

CMD chmod 755 ./start.sh
