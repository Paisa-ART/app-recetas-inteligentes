# Backend Dockerfile - Python/Django
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear carpetas necesarias
RUN mkdir -p staticfiles media logs

# Comando por defecto
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--max-requests", "1000", "--timeout", "30", "recetas_api.wsgi:application"]

# Expose puerto
EXPOSE 8000

# Health check - disable by setting HEALTHCHECK to none
# The gunicorn server is listening on 0.0.0.0:8000
