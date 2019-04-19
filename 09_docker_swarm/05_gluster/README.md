### Glusterfs (Inicialización)

En el nodo maestro
```
sudo gluster peer probe node1
sudo gluster peer probe node2
sudo gluster peer probe node3
gluster pool list
sudo gluster volume create swarm-vols replica 4 node0:/gluster/data node1:/gluster/data node2:/gluster/data node3:/gluster/data force
sudo gluster volume set swarm-vols auth.allow 127.0.0.1
sudo gluster volume start swarm-vols
```

En todos los nodos
```
sudo mount.glusterfs localhost:/swarm-vols /swarm/volumes
```

### Ejemplo Docker Swarm y Glusterfs

```
# ip=$(hostname -I | awk '{print $2}')
# docker swarm init --advertise-addr $ip
```

```
sudo docker node update --label-add nodename=node1 node1
sudo docker node update --label-add nodename=node2 node2
sudo docker node update --label-add nodename=node3 node3
mkdir /swarm/volumes/testvol
sudo docker service create --name testcon --constraint 'node.labels.nodename == node1' --mount type=bind,source=/swarm/volumes/testvol,target=/mnt/testvol busybox /bin/touch /mnt/testvol/testfile1.txt
sudo docker service ls
sudo docker service ps testcon
sudo docker service rm testcon
sudo docker service create --name testcon --constraint 'node.labels.nodename == node3' --mount type=bind,source=/swarm/volumes/testvol,target=/mnt/testvol busybox /bin/touch /mnt/testvol/testfile3.txt
sudo docker service ps testcon
ls -l /swarm/volumes/testvol/
```
