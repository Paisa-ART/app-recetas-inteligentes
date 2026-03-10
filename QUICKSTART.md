# 🚀 QUICKSTART - App Recetas Inteligentes

Guía rápida para ejecutar el proyecto completo.

## 📋 Tabla de Contenidos
1. [Con Docker (Recomendado)](#con-docker-recomendado)
2. [Sin Docker (Desarrollo Local)](#sin-docker-desarrollo-local)
3. [Troubleshooting](#troubleshooting)

---

## 🐳 Con Docker (Recomendado)

### Requisitos
- Docker
- Docker Compose

### Pasos

1. **Clonar el repositorio**
```bash
cd /workspaces/app-recetas-inteligentes
```

2. **Crear archivo .env**
```bash
cp .env.example .env
```

3. **Iniciar servicios**
```bash
docker-compose up --build
```

Espera a que todos los servicios estén "healthy" (~1-2 minutos).

4. **Acceder a la aplicación**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Admin: http://localhost:8000/admin

5. **Crear superusuario (una sola vez)**
```bash
docker-compose exec backend python manage.py createsuperuser
```

### Servicios Disponibles
- **Frontend**: React en puerto 3000
- **Backend**: Django en puerto 8000
- **PostgreSQL**: Puerto 5432
- **Redis**: Puerto 6379

### Comandos Útiles

Ejecutar migraciones:
```bash
docker-compose exec backend python manage.py migrate
```

Recolectar archivos estáticos:
```bash
docker-compose exec backend python manage.py collectstatic
```

Ver logs:
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

Detener servicios:
```bash
docker-compose down
```

---

## 💻 Sin Docker (Desarrollo Local)

### Requisitos
- Python 3.11+
- Node.js 18+
- PostgreSQL 13+
- Redis (opcional)

### Backend

1. **Instalar dependencias**
```bash
cd src/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configurar variables de entorno**
```bash
cp .env.example .env
```

Editá .env:
```env
DEBUG=True
SECRET_KEY=dev-secret-key
DB_NAME=recetas_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

3. **Ejecutar migraciones**
```bash
python manage.py migrate
```

4. **Crear superusuario**
```bash
python manage.py createsuperuser
```

5. **Ejecutar servidor**
```bash
python manage.py runserver
```

Backend en `http://localhost:8000`

### Frontend

1. **Instalar dependencias**
```bash
cd src/frontend
npm install
```

2. **Configurar variables de entorno**
```bash
cp .env.example .env
```

3. **Ejecutar servidor de desarrollo**
```bash
npm start
```

Frontend en `http://localhost:3000`

---

## 🔑 Cuentas de Prueba

### Admin
- Usuario: `admin`
- Contraseña: La que configuraste en `createsuperuser`

### Usuario Regular (crear en login)
- Ir a http://localhost:3000
- Hacer clic en "Registrarse"
- Completar formulario

---

## 📱 Pruebas Rápidas

### 1. Registrarse
```
Email: test@example.com
Usuario: testuser
Contraseña: TestPassword123
```

### 2. Crear Receta
1. Iniciar sesión
2. Ir a "Recetas"
3. Hacer clic en "Nueva Receta"
4. Completar formulario

### 3. Ajustar Porciones
1. Selecciona una receta
2. Cambia el número de personas
3. Ver cómo se ajustan automáticamente los ingredientes

### 4. Generar Lista de Compras
1. Abre una receta
2. Haz clic en "Generar Lista"
3. Descarga como PDF

---

## 🛠️ Troubleshooting

### Docker

**Port ya en uso**
```bash
# Cambiar puerto en docker-compose.yml
# Por ejemplo, cambiar 8000:8000 a 8001:8000
docker-compose down
docker-compose up
```

**Base de datos no sincroniza**
```bash
docker-compose down -v  # Elimina volúmenes
docker-compose up --build
```

**Contenedor no inicia**
```bash
docker-compose logs backend
docker-compose logs frontend
```

### Desarrollo Local

**Error: ModuleNotFoundError**
```bash
# Verificar venv activado
source venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

**PostgreSQL connection error**
```bash
# Verificar que PostgreSQL está corriendo
psql -U postgres -h localhost

# Actualizar .env con credenciales correctas
```

**Port 3000/8000 ya en uso**
```bash
# Encontrar proceso
lsof -i :3000
lsof -i :8000

# Matarlo
kill -9 <PID>
```

---

## 📚 Documentación Completa

- `src/backend/README.md` - Documentación backend
- `src/frontend/README.md` - Documentación frontend
- `docs/` - Documentación general del proyecto

---

## 🆘 Soporte

Si encuentras problemas:
1. Revisa este archivo
2. Consulta los READMEs específicos
3. Revisa los logs (`docker-compose logs`)
4. Abre un issue en GitHub

---

## ✨ ¡Listo!

Ya tienes todo configurado. ¡Comienza a crear recetas inteligentes! 🍲

Para parar los servicios:
```bash
docker-compose down
```

Para reanudar:
```bash
docker-compose up
```
