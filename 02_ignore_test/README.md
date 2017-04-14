### .dockerignore example

## Build image
docker build -t python_web .

## Run container
docker run -it -d --name python_web_01 python_web

## Options for accessing to docker container
docker exec -it python_web_01 bash

## Mount volumes from running container as specified in the Dockerfile in a busybox container
docker run --rm --volumes-from python_web_01 -t -i busybox sh
cd /home/python_user
python can't be executed because is not installed in busybox

## Backups
Ubuntu container is used as an intermediary to compress and uncompress the backup in the new container (python_web_02)
docker run --rm --volumes-from python_web_01 -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /home/python_user
Creates a new container named python_web_02 is expected that python_web_01 had populate the /home/python_user directory with new info
docker run -v /home/python_user --name python_web_02 python_web /bin/bash
Ubuntu container is used to mount the volume from python_web_02 and the backup located in the local directory. Then backup is uncompress
docker run --rm --volumes-from python_web_02 -v $(pwd):/backup ubuntu bash -c "cd /home/python_user && tar xvf /backup/backup.tar --strip 1"

Check if -v /home/python_user is neeeded because in the python_web image this volume is already mounted.

## Mount volume from running container in the host machine, volume is preserved even if container is removed
docker run -it -d -v /home/python_user --name python_web_01 python_web

This show the path where the volume is stored in the host machine
docker inspect python_web_01 | grep Source 

It doesn't overwrite the content of /home/python_user

### References
https://docs.docker.com/engine/reference/builder
https://docs.docker.com/engine/tutorials/dockervolumes
