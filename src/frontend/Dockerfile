# Frontend Dockerfile - React
# Stage 1: Build
FROM node:18-alpine AS builder

WORKDIR /app

# Variables de entorno
ENV CI=false
ENV NODE_OPTIONS=--max_old_space_size=4096

# Copiar package.json primero
COPY package.json ./

# Instalar dependencias
RUN npm install --no-audit --no-fund

# Copiar todo el código después
COPY public ./public
COPY src ./src

# Construir
RUN npm run build

# Stage 2: Servir
FROM node:18-alpine

WORKDIR /app

# Instalar serve
RUN npm install -g serve

# Copiar build desde builder
COPY --from=builder /app/build ./build

# Expose
EXPOSE 3000

# Health check - disable healthcheck since it can cause false failures
# The serve process is listening on port 3000

# Servir
CMD ["serve", "-s", "build", "-l", "3000"]
