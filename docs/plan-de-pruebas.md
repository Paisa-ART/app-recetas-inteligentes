# Plan de Pruebas

## Pruebas Unitarias

- Cálculo de cantidades (2 porciones → 4 porciones)
- Validación de emails
- Hash de contraseñas
- Cálculo de costos

**Herramienta:** pytest

## Pruebas de Integración

- Registro → Login usuario
- Crear receta → Aparece en biblioteca
- Ajustar porciones → Recalcula ingredientes
- Generar lista → Se descarga PDF

**Herramienta:** Django TestCase

## Pruebas de Funcionalidad

| Funcionalidad | Resultado esperado |
|---|---|
| Crear receta | Aparece en mi biblioteca |
| Ajustar porciones | Ingredientes se recalculan |
| Generar lista de compras | PDF descarga correctamente |
| Usar temporizador | Cuenta hacia atrás, alerta al terminar |
| Iniciar sesión | Acceso a la app |

**Herramienta:** Selenium

## Cronograma

| Semana | Tipo | Responsable |
|---|---|---|
| 1 | Unitarias | Backend |
| 2 | Integración | Backend |
| 3 | Funcionalidad | Tester |
| 4 | Todo | Equipo |

## Criterios de Aceptación

✅ 80% cobertura en pruebas unitarias  
✅ 0 bugs críticos  
✅ Todos los casos de funcionalidad pasan  
✅ App responde en menos de 3 segundos
