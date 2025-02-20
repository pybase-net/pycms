include .env

ENVIRONMENT ?= development
ROOT_DIR := $(shell pwd)
PORT ?= 1337

install: ## install dependencies
	@echo "Install dependencies"
	@uv sync
setup: ## setup
	@echo "Setup"
	@make install
run: ## run the application
	@echo "Run the application"
	@uv run python manage.py runserver ${PORT}
collectstatic: ## collect static files
	@echo "Collect static files"
	@python manage.py collectstatic