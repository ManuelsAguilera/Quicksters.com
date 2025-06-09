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
5. [Instrucciones de Ejecución](#instrucciones-de-ejecución)

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


## Objetivos Entrega Parcial

- **EP 2.1**: Creación del servidor en Node.js con Express o Flask
    - Creamos un servidor de flask, que maneja nuestra api REST, y se conecta a una base de datos local.
- **EP 2.2**: Configuración y modelado de la base de datos relacional.
    - Modelamos una base de datos relacional, y la implementamos en mysql
- **EP 2.3**: Desarrollo de API REST con endpoints básicos.
    - Hicimos los endpoints para cada tabla de nuestra base de datos, como un REST inicial.
- **EP 2.4**: Consumo de la API desde Ionic usando HttpClient.
    - La aplicacion, permite logearse, consumiendo de la api del servidor Flask. Tambien permite posteos en el caso del registro.
- **EP 2.5**: Implementación de autenticación con JWT (inicio de sesión/
registro)
    - Hacemos uso de un token de acceso con JWT a la hora de comprobar si el usuario es correcto
- **EP 2.6**: Validación de usuarios y manejo de sesiones.
    - Es posible loggearse dentro de la página web y mantener una sesión activa en conjunto a una opción de cerrar sesión.
- Avances no relacionados a entrega
    - Pasamos el proyecto a docker, para facilitar el compartir el proyecto compartiendo dependencias, y la misma base de datos.
    - Hicimos una base de datos local mysql que se despliega junto a docker.
    - Implementamos encriptacion usando bcrypt, para almacenar contraseñas encriptadas.
    - Hicimos pruebas en postman, para verificar que nuestra api funcione correctamente a la hora de acceder a datos de las tablas, y el proceso de autenticacion.

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