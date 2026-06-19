export PYTHONPATH := src

PYTHON     := python
RUFF       := ruff
DOCKER     := docker compose

.PHONY: help setup run cli lint test docker docker-build docker-down docker-logs clean

help:
	@echo "TypeSnake - available targets:"
	@echo ""
	@echo "  make setup        Install Python dependencies"
	@echo "  make run          Start Flask API server (localhost:8000)"
	@echo "  make cli          Run CLI version"
	@echo "  make lint         Lint with ruff"
	@echo "  make test         Run pytest"
	@echo "  make docker       Build and start Docker container (localhost:8000)"
	@echo "  make docker-down  Stop Docker container"
	@echo "  make docker-logs  Tail Docker logs"
	@echo "  make clean        Remove __pycache__ directories"
	@echo "  make help         Show this help"

setup:
	pip install -r requirements.txt

run:
	$(PYTHON) server/main.py

cli:
	$(PYTHON) server/app.py

lint:
	$(RUFF) check src/ server/

test:
	$(PYTHON) -m pytest

docker:
	$(DOCKER) up --build -d

docker-build:
	$(DOCKER) build

docker-down:
	$(DOCKER) down

docker-logs:
	$(DOCKER) logs -f

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
