# Production image of the blog: gunicorn serves main:app (same command as the Procfile).
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

COPY main.py ./
COPY src ./src

RUN useradd --create-home --uid 10001 blog && chown -R blog /app
USER blog

EXPOSE 8000
# FLASK_KEY and DB_URI come from the environment; PORT is optional (hosts set it).
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} main:app"]
