.PHONY: help build up down logs migrate createsuperuser test clean

help:
	@echo "App Recetas Inteligentes - Makefile"
	@echo "==================================="
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make build          - Construir imágenes Docker"
	@echo "  make up             - Iniciar servicios"
	@echo "  make down           - Detener servicios"
	@echo "  make logs           - Ver logs de los servicios"
	@echo "  make logs-backend   - Ver logs del backend"
	@echo "  make logs-frontend  - Ver logs del frontend"
	@echo "  make migrate        - Ejecutar migraciones"
	@echo "  make createsuperuser- Crear superusuario"
	@echo "  make test           - Ejecutar tests"
	@echo "  make clean          - Eliminar contenedores y volúmenes"
	@echo "  make bash-backend   - Acceder a shell del backend"
	@echo "  make bash-frontend  - Acceder a shell del frontend"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

migrate:
	docker-compose exec backend python manage.py migrate

createsuperuser:
	docker-compose exec backend python manage.py createsuperuser

test:
	docker-compose exec backend pytest

test-coverage:
	docker-compose exec backend pytest --cov=. --cov-report=html

clean:
	docker-compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

bash-backend:
	docker-compose exec backend bash

bash-frontend:
	docker-compose exec frontend bash

shell-backend:
	docker-compose exec backend python manage.py shell

collectstatic:
	docker-compose exec backend python manage.py collectstatic --noinput

lint:
	docker-compose exec backend pylint recipes users

format:
	docker-compose exec backend black .
