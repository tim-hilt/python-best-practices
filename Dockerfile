FROM python:3 AS builder

WORKDIR /app
COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    PATH="/root/.local/bin:$PATH" && \
    poetry config virtualenvs.in-project true && \
    poetry config virtualenvs.options.always-copy true && \
    poetry install

FROM gcr.io/distroless/static-debian12

WORKDIR /app
COPY --from=builder /app /app

ENTRYPOINT ["/app/.venv/bin/python", "-m", "python_best_practices"]
