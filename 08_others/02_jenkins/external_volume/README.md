### Jenkins

#### Description
Guide to deploy Jenkins version 2.19.1 LTS

#### Tutorial

Create a volume
```
docker volume create --name jenkins_workspace
```

Verify the creation of the volume
```
docker volume ls
```

Check the content of the volume using ubuntu or alpine base image
```
docker run -t -i -v jenkins_workspace:/tmp ubuntu /bin/bash
```
```
docker run -t -i -v jenkins_workspace:/tmp alpine /bin/sh
```

docker run -p 8080:8080 -p 50000:50000 -v jenkins_workspace:/var/jenkins_home jenkins:2.19.1

### Required plugins and description

pull request plugin
credentials plugin
restart plugin
github plugin
pipeline-dsl

###


https://clusterhq.com/2015/12/09/difference-docker-volumes-flocker-volumes/
https://docs.clusterhq.com/en/latest/docker-integration/
docker volume create -d flocker -o size=2GB --name jenkins_workspace


 docker volume rm
  docker volume ls -f dangling=true

remove anonympus volumes
  docker run --rm -v /foo -v awesome:/bar busybox top

  Volumes are only deleted if the container is removed with the docker rm -v command (the -v is essential) or the –rm flag was provided to docker run


docker-machine.exe ip
