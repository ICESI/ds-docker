# Guia

Despliegue la infraestructura y servicios en el swarm
```
docker stack deploy --compose-file docker-compose.yml stackdemo
```

Verificar que los servicios se estan ejecutando
```
docker stack services stackdemo
```

Actualice la cantidad de replicas en el archivo docker-compose.yml y ejecute el comando
```
docker stack deploy --compose-file docker-compose.yml stackdemo
```

Elimine la infraestructura y servicios creados
```
docker stack rm stackdemo
```

# Referencias
https://docs.docker.com/engine/reference/commandline/stack_deploy/#parent-command
