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

### Credenciales

Kibana default username and password:
```
username=elastic
password=changeme
```
