### Commands

En este ejemplo se observa como el contenedor toma el entrypoint de la imagen padre
```
$ docker pull ubuntu
$ docker run -it --name icesi_test ubuntu
#
```

En este ejemplo se observa como el contenido del volumen sobreescribe el contenido del contenedor,
y como el entrypoint del Dockerfile mantiene el microservicio activo
```
$ vi Dockerfile
$ docker build -t icesi_python .
$ docker run --restart always -d -p 8080:8080 -v $PWD/sources:/tmp --name icesi-test icesi_python
```
### Parameters



### References
https://hub.docker.com/_/ubuntu/
https://github.com/tianon/docker-brew-ubuntu-core/blob/46511cf49ad5d2628f3e8d88e1f8b18699a3ad8f/xenial/Dockerfile
