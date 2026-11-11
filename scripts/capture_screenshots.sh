#!/usr/bin/env bash
# Takes the lecture-step screenshots into docs/images/ without touching the desktop:
# the browser runs headless inside a Docker container (framework/process/gui-testing.md).
#
# Needs: Docker, a copy of .env.example as .env.docker, a fresh stack:
#   docker compose --env-file .env.docker down -v
#   docker compose --env-file .env.docker up -d --build
# Usage: bash scripts/capture_screenshots.sh
set -euo pipefail
cd "$(dirname "$0")/.."

ENV_FILE=".env.docker"
WEB_PORT="$(grep -E '^WEB_PORT=' "$ENV_FILE" | cut -d= -f2)"
WEB_PORT="${WEB_PORT:-8000}"
TERM_DIR="$(mktemp -d)"
trap 'rm -rf "$TERM_DIR"' EXIT

compose() { docker compose --env-file "$ENV_FILE" "$@"; }

# Terminal style steps: real command output, rendered as a terminal window.
{
	echo '$ git log --oneline'
	git log --oneline | head -12
} >"$TERM_DIR/02-commit-history.txt"
{
	echo '$ cat .env.example'
	grep -v -E '^(FLASK_KEY|POSTGRES_PASSWORD)=' .env.example
	echo 'FLASK_KEY=<generated secret, never committed>'
	echo 'POSTGRES_PASSWORD=<generated secret, never committed>'
	echo
	echo '$ sed -n "/def load_settings/,/return/p" src/infrastructure/config.py'
	sed -n '/def load_settings/,/return settings/p' src/infrastructure/config.py
} >"$TERM_DIR/03-environment-variables.txt"
{
	echo '$ cat Procfile'
	cat Procfile
	echo
	echo '$ docker compose logs web'
	compose logs --no-log-prefix web 2>&1 | grep -E 'Starting gunicorn|Listening|Booting worker' | sed -E 's/^\[[^]]*\] //'
} >"$TERM_DIR/04-procfile-gunicorn.txt"
{
	echo '$ git ls-files'
	git ls-files | grep -v '^framework' | head -40
} >"$TERM_DIR/05-repository-files.txt"
{
	echo '$ docker compose ps'
	compose ps --format 'table {{.Service}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
} >"$TERM_DIR/06-docker-compose.txt"
{
	echo '$ docker compose exec db psql -U blog -d blog -c "\dt"'
	compose exec -T db psql -U blog -d blog -c '\dt'
} >"$TERM_DIR/07-postgres-tables.txt"
{
	echo '$ python -m pytest -q'
	.venv/Scripts/python -m pytest -q 2>&1 | grep -E 'passed|failed'
} >"$TERM_DIR/09-tests.txt"

mkdir -p docs/images
MSYS_NO_PATHCONV=1 docker run --rm \
	--add-host host.docker.internal:host-gateway \
	-e BLOG_URL="http://host.docker.internal:${WEB_PORT}" \
	-v "$(pwd -W 2>/dev/null || pwd)/scripts/capture_screenshots.py:/work/capture_screenshots.py:ro" \
	-v "$(cd "$TERM_DIR" && (pwd -W 2>/dev/null || pwd) ):/terminal:ro" \
	-v "$(pwd -W 2>/dev/null || pwd)/docs/images:/out" \
	mcr.microsoft.com/playwright/python:v1.55.0-noble \
	sh -c 'python3 -m pip install -q playwright==1.55.0 && python3 /work/capture_screenshots.py'
ls docs/images
