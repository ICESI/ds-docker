Contruir el volumen postgresql:1.0

```
FROM ubuntu:16.04
MAINTAINER tebannew@gmail.com	

#Install package
RUN apt-get update -y
RUN apt-get install postgresql -y

#Configuracion del puerto de postgres
EXPOSE 5432
CMD postgresql -m http.server 5432
```

Para crear el volumen:
```
$ docker volume create --name postgresql_data
```

Para listar los volumenes creados:
```
$ docker volume ls
```

Conocer la ruta donde fue creado el volumen
```
$ docker volume inspect postgresql_data 
```

Iniciar un contenedor montando el volumen postgresql_data
```
$ docker run -it --rm -v postgresql_data:/var/lib/postgresql/9.5/main ubuntu_postgresql:1.0 /bin/bash
```

Iniciar el servicio de postgresql
```
# service postgresql start
```

Ingresar como el usuario posgres
```
# su postgres
```

Ingresar a postgresql
```
$ psql
```

Crear una base de datos
```
postgres=# CREATE DATABASE pruebaFuncionamiento;
```

Verifique que la base de datos ha sido creada
```
postgres=# \l
```

Obtener el directorio donde se almacenan los datos de postgresql
```
postgres=# show data_directory;
```

Para salir de postgresql
CTRL + D

Salir del contenedor virtual

Verificar que una vez destruido el contenedor los datos se encuentran en el volumen creado
```
$ ls /var/lib/docker/volumes/postgresql_data/_data
```

Cree un nuevo contenedor y verifique que la base de datos se ha recuperado a partir de los datos del volumen
```
$ docker run -it --rm -v postgresql_data:/var/lib/postgresql/9.5/main ubuntu_postgresql:1.0 /bin/bash
```

Algunas referencias
https://www.cyberciti.biz/faq/howto-add-postgresql-user-account/

