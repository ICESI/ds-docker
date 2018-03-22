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
root@2a709bf13cda:/#
```

En este ejemplo se observa como el contenido del volumen sobreescribe el contenido del contenedor,
y como el entrypoint del Dockerfile (directiva CMD) mantiene el microservicio activo
```
$ vi Dockerfile
$ docker build -t icesi_python .
$ docker run --restart always -d -p 8080:8080 -v $PWD/sources:/tmp --name icesi-test icesi_python
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
