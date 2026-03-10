# 🎉 App Recetas Inteligentes - COMPLETA Y FUNCIONANDO

## ✅ Estado de los Servicios

Todos los servicios están corriendo correctamente:

```
✓ Backend (Django + DRF)     en puerto 8000
✓ Frontend (React)           en puerto 3000
✓ PostgreSQL                 en puerto 5432
✓ Redis                      en puerto 6379
```

## 🚀 Acceder a la Aplicación

### Desde el Navegador en tu Máquina Host

**Option 1: Local Forward (Recomendado)**
```
Frontend: http://localhost:3000
Admin:    http://localhost:8000/admin
```

Si no funciona, intenta con el IP:
```
Frontend: http://127.0.0.1:3000
Admin:    http://127.0.0.1:8000/admin
```

### Credenciales de Administrador
```
Username: admin
Password: admin123
```

## 📋 API Endpoints

### Autenticación
- `POST /api/auth/register/` - Registrar nuevo usuario
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/me/` - Perfil del usuario

### Recetas
- `GET /api/recipes/` - Listar todas las recetas
- `POST /api/recipes/` - Crear nueva receta
- `GET /api/recipes/{id}/` - Obtener receta específica
- `PUT /api/recipes/{id}/` - Actualizar receta
- `DELETE /api/recipes/{id}/` - Eliminar receta

### Operaciones Especiales
- `POST /api/recipes/{id}/adjust_portions/` - Ajustar porciones
- `GET /api/recipes/{id}/generate_shopping_list/` - Generar lista de compras
- `POST /api/recipes/{id}/favorite/` - Guardar como favorita
- `GET /api/recipes/favorites/` - Ver recetas favoritas

## 🛠️ Comandos Útiles

### Ver logs en tiempo real
```bash
docker-compose logs -f backend    # Logs del backend
docker-compose logs -f frontend   # Logs del frontend
docker-compose logs -f postgres   # Logs de la BD
```

### Ejecutar comandos en el backend
```bash
# Crear migraciones
docker-compose exec backend python manage.py makemigrations

# Aplicar migraciones
docker-compose exec backend python manage.py migrate

# Acceder a Django shell
docker-compose exec backend python manage.py shell

# Crear superusuario adicional
docker-compose exec backend python manage.py createsuperuser
```

### Gestionar servicios
```bash
# Ver estado
docker-compose ps

# Reiniciar todos
docker-compose restart

# Parar todos
docker-compose down

# Reiniciar limpiamente
docker-compose down
docker-compose up -d

# Ver logs completos
docker-compose logs
```

## 🐛 Solucionar Problemas

### No puedo acceder a localhost:3000 o localhost:8000

1. Verifica que los contenedores estén corriendo:
   ```bash
   docker-compose ps
   ```

2. Si tienes "unhealthy", espera 30 segundos

3. Reinicia los servicios:
   ```bash
   docker-compose restart
   ```

### Error en las migraciones

```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

### Base de datos corrupta

```bash
docker-compose down
docker volume rm app-recetas-inteligentes_postgres_data
docker-compose up -d
```

## 📝 Próximas Acciones

1. **Accede al Admin**: http://localhost:8000/admin/
2. **Crea Recetas**: Ve a Recipes > Recipes y añade algunas recetas de fríjoles
3. **Prueba Frontend**: http://localhost:3000
4. **Prueba Registro**: Regístrate en la app
5. **Prueba Funcionalidades**:
   - Buscar y ver recetas
   - Ajustar porciones
   - Generar lista de compras
   - Guardar como favorita

## 🏗️ Arquitectura de la Aplicación

```
┌─────────────────────────────────────────┐
│          React Frontend (3000)          │
│  - Pages: Home, Login, Recipes, etc     │
│  - API Client: Axios + Interceptors     │
│  - Auth: Context API + localStorage     │
└────────────────┬────────────────────────┘
                 │ HTTP/REST
                 ▼
┌─────────────────────────────────────────┐
│     Django Backend API (8000)           │
│  - Recipes: CRUD + Adjustments          │
│  - Shopping Lists: Generation           │
│  - Users: Authentication (Token)        │
│  - Favorites: User Preferences          │
└────────────────┬────────────────────────┘
                 │ SQL
                 ▼
┌─────────────────────────────────────────┐
│    PostgreSQL 15 (5432)                 │
│    Redis 7 (6379) - Cache               │
└─────────────────────────────────────────┘
```

## 📊 Estructura de Base de Datos

### Modelos Principales

**Recipe**
- id, name, author, description
- portions, preparation_time, cooking_time
- difficulty_level, image

**Ingredient**
- id, recipe, name, quantity, unit
- cost (cálculos automáticos)

**Step**
- id, recipe, description, order
- preparation_time, cooking_time

**ShoppingList**
- id, user, created_at
- total_cost (calculado)

**FavoriteRecipe**
- id, user, recipe, created_at

**UserProfile**
- id, user (OneToOne)

## ✨ Características Implementadas

✅ Autenticación con Token
✅ CRUD de Recetas
✅ Ajuste de Porciones (cálculo automático)
✅ Generación de Listas de Compras
✅ Cálculo de Costos
✅ Gestión de Favoritos
✅ Admin Django completo
✅ CORS configurado
✅ API REST con DRF
✅ Frontend React moderno
✅ Docker Compose orchestration
✅ PostgreSQL + Redis
✅ Migraciones automáticas

---

**¡La aplicación está lista para usar! 🚀**

Si tienes algún problema, verifica los logs y asegúrate de que todos los contenedores tengan estado "Up" y "healthy".
