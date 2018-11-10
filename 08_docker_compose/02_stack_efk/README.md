### Guía

Ejecutar en el sistema anfitrión antes del despliegue
```
sudo sysctl -w vm.max_map_count=262144
```

Ejecutar el comando
```
docker-compose up
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
