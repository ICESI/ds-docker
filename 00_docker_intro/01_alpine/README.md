Dockerfile
```
FROM alpine
LABEL Daniel Barragan daniel.barragan@correo.icesi.edu.co

RUN apk add --no-cache apache2
RUN echo "ServerName 127.0.0.1" > /etc/apache2/conf.d/custom.conf
RUN mkdir -p /run/apache2

EXPOSE 80

ENTRYPOINT ["/usr/sbin/httpd"]
CMD ["-D", "FOREGROUND"]
```

Creación de imagen y contenedor
```
docker build -t icesi_web:0.0.1 .
docker images | grep icesi_web
docker run -d -p 8000:80 --name icesi_web icesi_web:0.0.1
docker ps
```
