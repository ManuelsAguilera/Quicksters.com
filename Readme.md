# Presentado por:
- Alex Alfaro
- Manuel Aguilera
- Vicente Rosales
- Eliseo Guarda 

# Aplicación web de speedruns

## Índice
1. [Resumen del Proyecto](#resumen-del-proyecto)
2. [Requerimientos](#requerimientos)
3. [Diseño de prototipos](#prototipo-de-diseño)
4. [Librerías en Angular](#librerías-usadas-con-angular)
5. [Objetivos Entrega Parcial](#Objetivos-Entrega-Parcial)
6. [Instrucciones de Ejecución](#instrucciones-de-ejecución)

## Resumen del Proyecto
Este sistema está diseñado para gestionar una plataforma competitiva de *speedruns*, donde los usuarios pueden subir sus tiempos, recibir validaciones por parte de administradores y ver reflejadas sus posiciones en rankings dinámicos. La aplicación permitirá también interacción comunitaria a través de foros, visualización de perfiles y personalización del usuario. Todo esto enfocado en fomentar la competitividad y la transparencia dentro del entorno de los videojuegos.

## Requerimientos

### Requerimientos Funcionales

| Tipo | ID | Título | Descripción |
|------|----|--------|-------------|
| Funcional | RF-01 | Gestión de puntaje de speedrunners | El sistema ajustará automáticamente el puntaje de los usuarios en función de su desempeño. Se sumarán puntos a quienes estén en el top 3 de cada categoría y se restarán a quienes no mantengan un rendimiento competitivo. |
| Funcional | RF-02 | Verificación de speedrun | El administrador podrá revisar y validar speedruns enviados por los usuarios según las reglas de cada categoría. Solo los validados impactan el puntaje. |
| Funcional | RF-03 | Subida de speedrun | Los usuarios podrán subir speedruns seleccionando el juego y la categoría. |
| Funcional | RF-04 | Actualización de tablas | La tabla de clasificación se actualizará automáticamente al validarse una nueva speedrun. |
| Funcional | RF-05 | Notificaciones automáticas a usuarios | El sistema notificará automáticamente a los usuarios ante eventos como: validación/rechazo de una speedrun, pérdida de récord, o respuestas en el foro. |
| Funcional | RF-06 | Control de permisos para subida de speedruns | Solo los usuarios autenticados podrán subir speedruns. |
| Funcional | RF-07 | Visualización de perfiles | Cualquier usuario podrá ver perfiles ajenos, incluyendo estadísticas, récords e icono de perfil. |
| Funcional | RF-08 | Publicación en foros | El sistema permitirá publicar y responder mensajes en los foros de cada juego o categoría. |
| Funcional | RF-09 | Registro de usuarios | Los nuevos usuarios podrán crear una cuenta con nombre, correo, usuario y contraseña. |
| Funcional | RF-10 | Inicio de sesión | Los usuarios podrán iniciar sesión usando correo y contraseña. |
| Funcional | RF-11 | Personalización de perfil | Los usuarios podrán cambiar su icono, editar su nombre y biografía, y decidir si mostrar estadísticas o récords. |

### Requerimientos No Funcionales

| Tipo | ID | Título | Descripción |
|------|----|--------|-------------|
| No funcional | RNF-01 | Plazo máximo de verificación de speedruns | Las speedruns deberán ser verificadas por un administrador en un máximo de 6 días calendario. |
| No funcional | RNF-02 | Soporte de usuarios concurrentes | El sistema debe poder manejar al menos **1000** usuarios conectados simultáneamente sin afectar el rendimiento. |
| No funcional | RNF-03 | Tiempos de respuesta | Las operaciones de navegación deben completarse en menos de 2 segundos en condiciones normales. |
| No funcional | RNF-04 | Interfaz clara para subidas de speedruns | La interfaz para subir speedruns debe ser clara y permitir completar el proceso en no más de **5 pasos**. |


## Prototipo de diseño 
[Figma - Prototipo de Quicksters](https://www.figma.com/design/jdAicbMdQMN6TOhtedVpKz/Quickster?node-id=6-68&m=dev)


## Librerías usadas con Angular

- **@ionic/angular**: Framework para construir aplicaciones móviles y web con Angular.
- **@angular/forms**: Módulo para manejar formularios reactivos y plantillas.
- **@capacitor/core**: Para integrar funcionalidades nativas en aplicaciones móviles.


# Objetivos Entrega Final: Funcionalidades avanzadas, optimizar rendimiento y preparar aplicación para su despliegue.

- **EF 1:** Implementación de funcionalidades completas (CRUD, notificaciones, almacenamiento local) de acuerdo a los requerimientos funcionales y no funcionales definidos.
- **EF 2:** Mejoras en UI/UX y optimización de rendimiento.
- **EF 3:** Implementación de seguridad avanzada en API: protección contra inyección SQL/XSS, implementación CORS seguro, y encriptación de datos sensibles con bcrypt.
- **EF 4:** Optimización de consultas y respuesta eficiente.
- **EF 5:** Integración con algún servicio externo (AWS o APIs de terceros).
- Entrega:
    - Aplicación con CRUD completo, UI/UX optimizado y seguridad web aplicada.
    - Backend seguro con validaciones y cifrado de datos.
    - Documentación técnica del proyecto.



# Instrucciones de Ejecución
## Instrucciones usando Docker (Recomendada)
1. Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clonar el repositorio:
   ```bash
   git clone https://github.com/ManuelsAguilera/Quicksters.com.git
   cd Quicksters.com
   ```
3. Iniciar los servicios:
   ```bash
   docker-compose up --build
   ```
4. Acceder a la aplicación:
   - Frontend: http://localhost:8100
   - API: http://localhost:5000 

Los servicios disponibles son:
- Frontend (Ionic/Angular)
- Backend (Flask API)
- Base de datos (MySQL)


## Opcion local (Sin docker)

### Requisitos previos
1. Node.js (versión 16 o superior)
2. Angular CLI: `npm install -g @angular/cli`
3. Python 3.10 o superior
4. MySQL


1. Instalar dependencias del frontend:
   ```bash
   cd frontend
   npm install
   ionic serve
   ```
2. Instalar dependencias del backend:
   ```bash
   cd backends
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   python src/app.py
   ```