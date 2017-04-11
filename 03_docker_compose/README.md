### Introducción a docker-compose
Universidad ICESI  
Curso: Sistemas Distribuidos
Docente: Daniel Barragán C.  
Tema: Introducción a despliegue de ambientes con docker-compose  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Desplegar ambientes empleando docker-compose

### Introducción
La tecnología docker-compose permite el despliegue de ambientes conformados por contenedores virtuales. Se emplea un archivo en formato yaml para la especificación de la infraestructura a desplegar.

### Desarrollo

#### Comandos comunes

| Comando   | Descripción   |
|---|---|
| docker-compose up | ejecutar el ambiente |
| docker-compose up -d | ejecutar el ambiente en modo desligado |
| docker-compose ps | listar los contenedores del ambiente |
| docker-compose run web env | |
| docker-compose stop | detener el ambiente |
| docker-compose down --volumes | destruir el ambiente |
