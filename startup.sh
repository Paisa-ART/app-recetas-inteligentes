#!/bin/bash
set -e

cd /workspaces/app-recetas-inteligentes

echo "=== Docker Compose Status ==="
docker-compose ps

echo ""
echo "=== Starting Services ==="
docker-compose up -d --remove-orphans

echo ""
echo "=== Waiting for services to start ==="
sleep 10

echo ""
echo "=== Service Status ==="
docker-compose ps

echo ""
echo "=== Backend Logs ==="
docker-compose logs backend | tail -30

echo ""
echo "=== Frontend Logs ==="
docker-compose logs frontend | tail -30

echo ""
echo "=== Testing Connectivity ==="
echo "Backend: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:8000/admin/ 2>/dev/null || echo 'FAILED')"
echo "Frontend: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:3000 2>/dev/null || echo 'FAILED')"
