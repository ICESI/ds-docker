### Ejemplo Docker Swarm y Glusterfs

Para la realización de los pasos siguientes se requiere haber desplegado un cluster de glusterfs como se explica en el repositorio
ICESI/ds-glusterfs

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

### Referencias
* http://embaby.com/blog/using-glusterfs-docker-swarm-cluster/
* https://docs.gluster.org/en/latest/Quick-Start-Guide/Quickstart/
* http://ask.xmodulo.com/create-mount-xfs-file-system-linux.html
* https://www.cyberciti.biz/faq/linux-how-to-delete-a-partition-with-fdisk-command/
* https://support.rackspace.com/how-to/getting-started-with-glusterfs-considerations-and-installation/
* https://everythingshouldbevirtual.com/virtualization/vagrant-adding-a-second-hard-drive/
