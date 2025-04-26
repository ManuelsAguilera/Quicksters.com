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

---

### Requerimientos No Funcionales

| Tipo | ID | Título | Descripción |
|------|----|--------|-------------|
| No funcional | RNF-01 | Plazo máximo de verificación de speedruns | Las speedruns deberán ser verificadas por un administrador en un máximo de 6 días calendario. |
| No funcional | RNF-02 | Soporte de usuarios concurrentes | El sistema debe poder manejar al menos **1000** usuarios conectados simultáneamente sin afectar el rendimiento. |
| No funcional | RNF-03 | Tiempos de respuesta | Las operaciones de navegación deben completarse en menos de 2 segundos en condiciones normales. |
| No funcional | RNF-04 | Interfaz clara para subidas de speedruns | La interfaz para subir speedruns debe ser clara y permitir completar el proceso en no más de **5 pasos**. |

## Prototipo de diseño 
[Figma - Prototipo de Quicksters](https://www.figma.com/design/jdAicbMdQMN6TOhtedVpKz/Quickster?node-id=94-648&m=dev)

---

## Librerías usadas con Angular

- **@ionic/angular**: Framework para construir aplicaciones móviles y web con Angular.
- **@angular/forms**: Módulo para manejar formularios reactivos y plantillas.
- **@capacitor/core**: Para integrar funcionalidades nativas en aplicaciones móviles.

---

## Instrucciones de Ejecución

### Requisitos previos
1. Tener instalado [Node.js](https://nodejs.org/) (versión 16 o superior).
2. Tener instalado Angular CLI:
   ```bash
   npm install -g @angular/cli
# pasos para ejecutar 
Pasos para ejecutar el proyecto
1. Clona el repositorio: git clone <https://github.com/ManuelsAguilera/Quicksters.com.git>
2. Instala las dependencias: npm install
3. Inicia el servidor de desarrollo:ionic serve
   
