# --------------------- Base stage ---------------------
FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get purge -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy only the dependency files first
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry install --no-root

# --------------------- Builder stage ---------------------
FROM base AS builder

COPY . /app
RUN poetry install

# --------------------- Final stage ---------------------
FROM python:3.13-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

# Copy app and installed packages from builder
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Set correct permissions for the non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set entrypoint
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
