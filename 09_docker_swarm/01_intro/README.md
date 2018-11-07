### Guía

Debido a que docker swarm se ejecuta en múltiples nodos, es necesario usar un registry en internet o desplegar
un registry privado como se muestra a continuación:
```
docker service create --name registry --publish published=5000,target=5000 registry:2
```

Para verificar el estado del registry desplegado use el comando
```
docker service ls
```

Verificar la respuesta del registry por medio del comando curl
```
curl http://localhost:5000/v2/
```

Los siguientes pasos permiten probar la aplicación de conteo con flask y redis en forma local.
Despliegue la infraestructura y servicios
```
docker-compose up -d
```

Visualize los componentes desplegados
```
docker-compose ps
```

Verifique la respuesta del servicio desplegado 
```
curl http://localhost:8000
```

Elimine la infraestructura y servicios
```
docker-compose down --volumes
```

Los siguientes pasos permiten probar la aplicación de conteo con flask y redis en el swarm
Publique la imagen del servicio en el registry local
```
docker-compose push
```

Despliegue la infraestructura y servicios en el swarm
```
docker stack deploy --compose-file docker-compose.yml stackdemo
```

Verificar que los servicios se estan ejecutando
```
docker stack services stackdemo
```

Verifique la respuesta del servicio desplegado usando como url el localhost o la ip de alguno de los equipos del swarm
```
curl http://localhost:8000
curl http://address-of-other-node:8000
```

Elimine la infraestructura y servicios creados
```
docker stack rm stackdemo
```

Elimine el registry
```
docker service rm registry
```

Abandone el swarm en los nodos workers
```
docker swarm leave --force
```

### References
* https://docs.docker.com/engine/swarm/stack-deploy/
