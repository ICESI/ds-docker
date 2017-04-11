### Introducción al despliegue de aplicaciones de tres capas con docker-compose
Universidad ICESI  
Curso: Sistemas Distribuidos
Docente: Daniel Barragán C.  
Tema: Introducción al despliegue de aplicaciones de tres capas con docker-compose  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Desplegar aplicaciones de tres capas empleando docker-compose

### Introducción
En esta guía se muestra un ejemplo de como desplegar una aplicación de tres capas empleando docker-compose.

### Desarrollo

Ejecute las siguientes instrucciones

```
$ docker-compose up
$ docker ps
$ docker exec -it id_container_flask /bin/bash
$ cd scripts
$ python dbmanage.py create
$ exit
$ curl http://127.0.0.1:8080/smartlabs/api/v1.0/devices/SN0001
```
