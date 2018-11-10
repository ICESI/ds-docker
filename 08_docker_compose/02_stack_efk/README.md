### Guía

Ejecutar en el sistema anfitrión antes del despliegue
```
sudo sysctl -w vm.max_map_count=262144
```

Ejecutar el comando
```
docker-compose up
```

Sí realiza cambios a los archivos Dockerfile deberá desplegar el stack con el comando
```
docker-compose up --build
```

Verificar que todos los contenedores se encuentran activos
```
docker ps
```

### Notas

El archivo jvm.options mantiene un limite para la memoria que se puede asignar a elasticsearch
para ampliarla emplee las siguientes instrucciones dentro del contenedor de elasticsearch 

```
vi /usr/share/elasticsearch/config/jvm.options
# Xms represents the initial size of total heap space
# Xmx represents the maximum size of total heap space
-Xms1g
-Xmx1g
```

### Credenciales

Kibana default username and password:
```
username=elastic
password=changeme
```

### Referencias
* https://docs.fluentd.org/v1.0/articles/quickstart
* https://rubygems.org/gems/fluent-plugin-elasticsearch
* https://hub.docker.com/r/fluent/fluentd/
* https://github.com/cdcardenas/sd-exam3
