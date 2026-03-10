# Backend - App Recetas Inteligentes

Backend API REST desarrollado con **Django** y **Django Rest Framework**.

## 📋 Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## ⚙️ Requisitos

- Python 3.11+
- PostgreSQL 13+
- Redis (opcional para caché)
- pip / virtualenv

## 🚀 Instalación

### 1. Crear ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tus configuraciones
```

### 4. Ejecutar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

## 🔧 Configuración

### Variables de Entorno (.env)

```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=recetas_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## 🎯 Ejecución

### Desarrollo
```bash
python manage.py runserver
```

La API estará en: `http://localhost:8000`

### Producción
```bash
gunicorn recetas_api.wsgi:application --bind 0.0.0.0:8000
```

## 📡 API Endpoints

### Autenticación
- `POST /api/auth/users/register/` - Registrar usuario
- `POST /api/auth/users/login/` - Iniciar sesión
- `POST /api/auth/users/logout/` - Cerrar sesión
- `GET /api/auth/users/me/` - Perfil del usuario

### Recetas
- `GET /api/recipes/` - Listar todas las recetas
- `POST /api/recipes/` - Crear receta
- `GET /api/recipes/{id}/` - Obtener receta
- `PATCH /api/recipes/{id}/` - Actualizar receta
- `DELETE /api/recipes/{id}/` - Eliminar receta

### Funcionalidades
- `POST /api/recipes/{id}/adjust_portions/` - Ajustar porciones
- `POST /api/recipes/{id}/generate_shopping_list/` - Generar lista de compras
- `POST /api/recipes/{id}/favorite/` - Agregar a favoritas
- `DELETE /api/recipes/{id}/favorite/` - Remover de favoritas
- `GET /api/recipes/favorites/` - Obtener favoritas

### Listas de Compras
- `GET /api/recipes/shopping-lists/` - Listar listas
- `GET /api/recipes/shopping-lists/{id}/` - Obtener lista
- `GET /api/recipes/shopping-lists/{id}/export_pdf/` - Exportar a PDF

## ✅ Testing

### Pruebas Unitarias
```bash
pytest tests/unit/
```

### Pruebas de Integración
```bash
pytest tests/integration/
```

### Cobertura
```bash
pytest --cov=.
```

## 📁 Estructura del Proyecto

```
backend/
├── recetas_api/          # Configuración principal
│   ├── settings.py       # Configuraciones
│   ├── urls.py           # Rutas principales
│   └── wsgi.py           # WSGI app
├── recipes/              # App de recetas
│   ├── models.py         # Modelos
│   ├── serializers.py    # Serializadores
│   ├── views.py          # Vistas
│   ├── urls.py           # Rutas
│   └── admin.py          # Admin
├── users/                # App de usuarios
│   ├── models.py         # Modelos
│   ├── serializers.py    # Serializadores
│   ├── views.py          # Vistas
│   ├── urls.py           # Rutas
│   └── admin.py          # Admin
├── manage.py             # Utilidad Django
├── requirements.txt      # Dependencias
├── .env.example          # Ejemplo de env
└── Dockerfile            # Docker
```

## 🐳 Docker

### Build
```bash
docker build -t recetas-backend .
```

### Run
```bash
docker run -p 8000:8000 recetas-backend
```

## 📚 Documentación Adicional

- [Django Docs](https://docs.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/docs/)
