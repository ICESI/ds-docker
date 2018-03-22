### Commands

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

### Parameters
-d: modo deattach  
-p: reenvío de puertos anfitrión:contenedor  
-v: montaje de volumenes directorio_anfitrión:directorio_contenedor  
--name: nombre del contenedor  
--restart always: reiniciar el contenedor si este es apagado abruptamente  

### Activities
1. Investigue la forma de reenviar logs de un contenedor hacia fluentd

### References
https://hub.docker.com/_/ubuntu/
https://github.com/tianon/docker-brew-ubuntu-core/blob/46511cf49ad5d2628f3e8d88e1f8b18699a3ad8f/xenial/Dockerfile
