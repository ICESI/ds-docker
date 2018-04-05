### Introducción a la virtualización con contenedores virtuales

Universidad ICESI  
Curso: Sistemas Distribuidos  
Docente: Daniel Barragán C.  
Tema: Introducción a la virtualización con contenedores virtuales  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer la estructura básica de los archivos Dockerfile
* Entender el concepto de punto de entrada (entrypoint) y su importancia en la virtualización con contenedores
* Emplear volúmenes para compartir archivos entre el sistema anfitrión y los contenedores
* Desplegar microservicios empleando contenedores virtuales

### Guía
La imagen de alpine es una de las images con menor tamaño en docker hub, ideal para el despliegue de microservicios
```
$ docker pull alpine
$ docker images | grep alpine
4.15 MB
```

En este ejemplo se observa como el contenedor toma el entrypoint (directiva CMD) de la imagen padre
```
$ docker pull ubuntu
$ docker run -it --name icesi_test ubuntu
root@d80ca057de18:/# uname -S
Linux
root@d80ca057de18:/# exit
```

El contenedor se detiene una vez se ejecuta el comando exit. Para eliminar el contenedor detenido haga lo
siguiente:
```
$ docker ps -a | grep icesi_test
d80ca057de18
$ docker rm d80ca057de18
```

En este ejemplo se observa como el contenido del volumen sobrescribe el contenido del contenedor,
y como el entrypoint del Dockerfile (directiva CMD) mantiene el microservicio activo
```
$ vi Dockerfile
$ docker build -t icesi_web .
$ docker run --restart always -d -p 8080:80 -v $PWD/html:/var/www/html --name icesi_test icesi_web
```

Para ingresar al contenedor en ejecución digite los siguientes comandos:

```
docker ps | grep icesi_test
d80ca057de18
docker exec -it d80ca057de18 /bin/bash
root@d80ca057de18:/# cd /var/www/html
root@d80ca057de18:/# ls
root@d80ca057de18:/# exit
```

Para forzar la eliminación de un contenedor que se encuentra en ejecución haga lo siguiente:
```
$ docker ps | grep icesi_test
d80ca057de18
$ docker rm -f d80ca057de18
```

Una ópcion muy empleada con docker es la creación de volumenes. Emplee los siguientes
comandos para crear un volumen y montar sus archivos en un contenedor
```
$ docker volume create html_files
$ sudo su
# cd /var/lib/docker/volumes/html_files/_data
# wget www.icesi.edu.co
# ls -l index.html
# exit
$ docker run -d -p 8080:80 -v html_files:/var/www/html --name icesi_test icesi_web
```

### Parámetros
-d: modo deattach  
-p: reenvío de puertos anfitrión:contenedor  
-v: montaje de volumenes directorio_anfitrión:directorio_contenedor  
--name: nombre del contenedor  
--restart always: reiniciar el contenedor si este es apagado abruptamente  

### Actividades
1. Investigue acerca de las mejores prácticas al crear contenedores virtuales
2. Reemplace todas las directivas RUN por una sola (concatene todos los comandos). Realice una
comparación del tamaño de la imagen creada con todas las directivas RUN contra la creada con una
sola directiva RUN. Que se puede concluir al respecto?
3. Investigue la forma de reenviar logs de un contenedor hacia fluentd

### Referencias
https://hub.docker.com/_/ubuntu/  
https://github.com/tianon/docker-brew-ubuntu-core/blob/46511cf49ad5d2628f3e8d88e1f8b18699a3ad8f/xenial/Dockerfile  
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint
