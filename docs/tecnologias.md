2. Lenguajes de Programación

La solución busca aprovechar las fortalezas de cada lenguaje: JavaScript en el cliente, Python en el servidor y Java como alternativa de escalabilidad.

### 2.1 JavaScript

**Justificación:** Ideal para el frontend, permite crear interfaces interactivas y modernas, facilitando la experiencia del usuario.
---

### 2.2 Python

**Justificación:** Excelente para el backend, por su rapidez de desarrollo, seguridad y gran comunidad de soporte. Su comunidad activa reduce significativamente el tiempo de desarrollo. Python facilita la escritura de código, aspecto clave cuando se trabaja en equipo con plazos ajustados.

---

### 2.3 Java *(referencial)*

**Justificación:** Lenguaje robusto y ampliamente usados en el desarrollo web y de aplicaciones. Permiten flexibilidad y escalabilidad.

---

## 3. Frameworks de Desarrollo

### 3.1 React (JavaScript)

**Tipo:** Biblioteca de JavaScript para construcción de interfaces de usuario basadas en componentes.

**Justificación técnica:**
- Utiliza un **Virtual DOM** que actualiza únicamente las partes de la pantalla que cambian, ofreciendo una experiencia de usuario ágil.
- Arquitectura basada en **componentes reutilizables**, lo que facilita el mantenimiento y la escalabilidad del código.
- Gran comunidad de soporte, abundante documentación y ecosistema de herramientas complementarias (React Router, Axios).
- Curva de aprendizaje accesible para el equipo y alto nivel de demanda en el mercado laboral.

---

### 3.2 Django (Python)

**Tipo:** Framework web de alto nivel que sigue el patrón MVT (Model-View-Template).

**Justificación técnica:**
- Ofrece un **ORM integrado** que abstrae las consultas SQL y simplifica las operaciones sobre la base de datos.
- Incluye protecciones de seguridad activas por defecto: CSRF, XSS, inyección SQL.
- El **panel de administración automático** permite gestionar el contenido del sistema sin desarrollar una interfaz adicional.
- Se integra de forma natural con Python, el lenguaje de scripting del proyecto, unificando el stack del servidor.

---

## 4. Repositorio y Control de Versiones

### 4.1 GitHub

**Rol en el proyecto:** Repositorio central del código fuente del sistema, punto de colaboración entre los integrantes del equipo y base para la integración continua en fases futuras.

**Justificación técnica:**
- Proporciona **control de versiones distribuido** con Git, permitiendo que cada desarrollador trabaje localmente y sincronice cambios sin pérdida de información.
- Los **Pull Requests** habilitan la revisión de código entre pares antes de integrar cambios a la rama principal, mejorando la calidad del producto.
- El sistema de **Issues** facilita el registro y seguimiento de errores, mejoras y tareas pendientes directamente vinculadas al código.
- Compatible con **GitHub Actions** para automatizar pruebas y despliegues en el futuro.

### 4.2 Flujo de trabajo en GitHub

| Rama | Propósito |
|------|-----------|
| `main` | Código estable y listo para producción |
| `develop` | Integración de nuevas funcionalidades antes de pasar a main |
| `feature/nombre` | Desarrollo aislado de una funcionalidad específica |
| `hotfix/nombre` | Corrección urgente de errores en producción |

---

## 5. Gestión del Proyecto

### 5.1 Trello

**Justificación técnica:**
- Ofrece una **organización visual tipo tablero** que permite ver de un vistazo el estado de cada tarea y detectar cuellos de botella.
- Facilita la **asignación de responsables**, fechas límite y etiquetas de prioridad por tarjeta.
- Se adapta a metodologías ágiles (Scrum/Kanban), permitiendo dividir el trabajo en sprints con objetivos claros.
- Acceso gratuito, sin instalación y disponible en web y móvil.

### 5.2 Estructura del tablero Trello

| Columna | Descripción |
|---------|-------------|
| **Backlog** | Listado completo de historias de usuario identificadas |
| **Por hacer** | Tareas planificadas para el sprint actual |
| **En progreso** | Tareas que un miembro del equipo está ejecutando |
| **En revisión** | Tareas finalizadas pendientes de validación |
| **Hecho** | Tareas completadas y aceptadas por el equipo |

---

## 6. Herramientas de Modelado

### 6.1 Draw.io

**Justificación técnica:**
- No requiere instalación obligatoria; funciona directamente en el navegador.
- Soporta exportación en formatos estándar: PNG, SVG y PDF.
- Los archivos de diagrama (`.drawio`) pueden versionarse en GitHub junto con el código fuente.
- Interfaz intuitiva que permite la colaboración simultánea entre miembros del equipo.

---

### 6.2 StarUML

**Justificación técnica:**
- Sigue los estándares UML de la industria, garantizando que los modelos sean comprensibles por cualquier ingeniero de software.
- Permite generar código esqueleto a partir de los diagramas de clases, acelerando la fase de implementación.
- Ofrece una interfaz visual dedicada al modelado que facilita la creación de diagramas complejos con precisión.

---

## 7. Resumen de la Pila Tecnológica

| Categoría | Herramienta | Rol en el Proyecto |
|-----------|-------------|-------------------|
| Frontend | JavaScript + React | Interfaces interactivas y dinámicas |
| Backend | Python + Django | API REST, lógica de negocio y seguridad |
| Lenguaje alternativo | Java | Escalabilidad futura del servidor |
| Repositorio | GitHub | Control de versiones y colaboración |
| Gestión ágil | Trello | Planificación y seguimiento Kanban |
| Modelado UML | StarUML | Diagramas técnicos formales |
| Modelado visual | Draw.io | Arquitectura y flujos de usuario |