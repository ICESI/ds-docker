```
docker pull sameersbn/bind
docker run -d --name=bind --dns=127.0.0.1 \
  --publish=172.17.42.1:53:53/udp --publish=172.17.42.1:10000:10000 \
  --volume=/srv/docker/bind:/data \
  --env='ROOT_PASSWORD=SecretPassword' \
  sameersbn/bind:latest
```

```
docker pull sameersbn/bind
docker run -d --name=bind --dns=127.0.0.1 \
  --publish=172.17.0.1:53:53/udp --publish=172.17.0.1:10000:10000 \
  --volume=/srv/docker/bind:/data \
  --env='ROOT_PASSWORD=SecretPassword' \
  sameersbn/bind:latest
```

### Referencias
* http://www.damagehead.com/blog/2015/04/28/deploying-a-dns-server-using-docker/
* https://hub.docker.com/r/sameersbn/bind/
