FROM python:3.7.3-alpine3.9

ARG TOKEN
ARG GRAPHQL_ENDPOINT
ARG PREFIX

ENV TOKEN = $TOKEN \
    GRAPHQL_ENDPOINT = $GRAPHQL_ENDPOINT \
    PREFIX = $PREFIX

RUN apk add curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app
COPY poetry.lock .
COPY pyproject.toml .

RUN  /root/.poetry/bin/poetry  config settings.virtualenvs.create false \
    &&  /root/.poetry/bin/poetry  install --no-dev --no-interaction --no-ansi

COPY . .

CMD ["/root/.poetry/bin/poetry", "run", "start"]
