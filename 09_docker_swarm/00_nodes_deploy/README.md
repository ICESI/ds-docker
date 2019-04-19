# Guia

En el nodo maestro inicializar el cluster de docker swarm
```
ip=$(hostname -I | awk '{print $2}')
docker swarm init --advertise-addr $ip
```

Obtener en el nodo maestro el comando para adicionar un nuevo nodo al swarm (este comando tambien se obtiene al ejecutar el comando para inicializar el cluster)
```
docker swarm join-token worker
```

Adicionar el nodo
```
docker swarm join \
  --token  SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
  192.168.99.100:2377
```

Ver el estado del swarm
```
docker info
```

Ver el estado de los nodos
```
docker node ls
```

Crear una tarea en el swarm
```
docker service create --replicas 1 --name <SERVICE-ID> alpine ping docker.com
```

Validar que se ha desplegado la tarea
```
docker service ls
```

Despliegue los detalles de un servicio
```
docker service inspect --pretty <SERVICE-ID>
```

Observe los logs del servicio
```
docker service logs <SERVICE-ID> -f
```

Observe los nodos que estan ejecutando el servicio
```
docker service ps <SERVICE-ID>
```

Actualice la cantidad de replicas del servicio
```
docker service scale <SERVICE-ID>=<NUMBER-OF-TASKS>
```

Observe los cambios, note los nodos en los que se esta ejecutando el servicio
```
docker service ps <SERVICE-ID>
```

Desactive uno de los nodos
```
docker node update --availability drain <NODE-ID>
```

Verifique la disponibilidad del nodo
```
docker node inspect --pretty <NODE-ID>
```

Observe nuevamente el estado del servicio en el swarm
```
docker service ps <SERVICE-ID>
```

Reactive el nodo
```
docker node update --availability active <NODE-ID>
```

Verifique la disponibilidad del nodo
```
docker node inspect --pretty <NODE-ID>
```

Elimine el servicio
```
docker service rm <SERVICE-ID>
```

## Service discovery

Crea la siguiente tarea en el swarm
```
docker service create --name lbapp1 --replicas 2 -p 81:80 katacoda/docker-http-server
```

Realice peticiones
```
curl docker:81
```

Escale el cluster
```
docker service scale lbapp1=3
```

Listar los servicios del swarm
```
docker service ls
```

## Networks

Liste las redes del swarm
```
docker network ls
```

# Referencias
* https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/
* https://www.katacoda.com/courses/docker-orchestration/load-balance-service-discovery-swarm-mode
* https://training.play-with-docker.com/swarm-service-discovery/
* https://docs.docker.com/engine/swarm/ingress/
