# Frontend - App Recetas Inteligentes

Interfaz web desarrollada con **React 18**, **React Router** y **Tailwind CSS**.

## 📋 Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Componentes Principales](#componentes-principales)
- [Testing](#testing)

## ⚙️ Requisitos

- Node.js 18+
- npm 9+ o yarn 3+
- Backend ejecutándose en `http://localhost:8000`

## 🚀 Instalación

### 1. Instalar dependencias
```bash
npm install
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tus configuraciones
```

### Variables de Entorno (.env)

```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_API_TIMEOUT=30000
REACT_APP_DEBUG=false
```

## 🎯 Ejecución

### Desarrollo
```bash
npm start
```

La aplicación estará en: `http://localhost:3000`

### Build de Producción
```bash
npm run build
```

Esto crea una carpeta `build/` optimizada para producción.

### Servir Build Localmente
```bash
npm install -g serve
serve -s build
```

## 📁 Estructura del Proyecto

```
frontend/
├── public/               # Archivos estáticos
│   └── index.html        # HTML principal
├── src/
│   ├── api/              # Servicios de API
│   │   ├── client.js     # Configuración de axios
│   │   └── services.js   # Servicios de API
│   ├── hooks/            # Custom hooks
│   │   └── useAuth.js    # Hook de autenticación
│   ├── components/       # Componentes reutilizables
│   │   └── Nav.jsx       # Barra de navegación
│   ├── pages/            # Páginas principales
│   │   ├── Home.jsx      # Página inicial
│   │   └── Login.jsx     # Página de login
│   ├── App.jsx           # Componente principal
│   ├── index.js          # Punto de entrada
│   └── index.css         # Estilos globales
├── package.json          # Dependencias
├── .env.example          # Ejemplo de env
├── Dockerfile            # Docker
└── README.md             # Este archivo
```

## 🧩 Componentes Principales

### Nav
Componente de navegación con autenticación.

### Home
Página de bienvenida que muestra las características principales.

### Login
Formulario de inicio de sesión con validación.

## 🔐 Autenticación

El sistema usa tokens de autenticación que se almacenan en `localStorage`.

### Flujo de Login
1. Usuario ingresa credenciales
2. Backend devuelve token
3. Token se guarda en localStorage
4. Se añade automaticamente a cada petición en headers

### Flujo de Logout
1. Usuario hace clic en "Salir"
2. Token se elimina de localStorage
3. Usuario es redirigido a "/login"

## 🎨 Estilos

El proyecto usa **Tailwind CSS** para estilos.

### Clases Personalizadas (en index.css)
```css
.btn-primary      /* Botón principal */
.btn-secondary    /* Botón secundario */
.card             /* Tarjeta */
.input-field      /* Campo de entrada */
```

## 🧪 Testing

### Ejecutar tests
```bash
npm test
```

### Tests disponibles
- Componentes
- Hooks
- Servicios de API
- Integración

## 🐳 Docker

### Build
```bash
docker build -t recetas-frontend .
```

### Run
```bash
docker run -p 3000:3000 recetas-frontend
```

## 📦 Dependencias Principales

- **react**: UI library
- **react-router-dom**: Enrutamiento
- **axios**: Cliente HTTP
- **tailwindcss**: Estilos CSS
- **react-icons**: Iconos
- **date-fns**: Manejo de fechas

## 🚀 Deploy

### Vercel
```bash
vercel
```

### Netlify
```bash
npm run build
# Sube la carpeta 'build' a Netlify
```

### Docker
```bash
docker build -t recetas-frontend .
docker run -d -p 80:3000 recetas-frontend
```

## 📚 Documentación Adicional

- [React Docs](https://react.dev)
- [React Router](https://reactrouter.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)
