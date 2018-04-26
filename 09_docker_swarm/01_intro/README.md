### Guía

```
$ docker service create --name registry --publish published=5000,target=5000 registry:2
$ docker service ls
$ curl http://localhost:5000/v2/
$ docker-compose up -d
$ docker-compose ps
$ curl http://localhost:8000
$ docker-compose down --volumes
$ docker-compose push
$ docker stack deploy --compose-file docker-compose.yml stackdemo
$ docker stack services stackdemo
$ curl http://localhost:8000
$ curl http://address-of-other-node:8000
$ docker stack rm stackdemo
$ docker service rm registry
$ docker swarm leave --force
```

### References
* https://docs.docker.com/engine/swarm/stack-deploy/
