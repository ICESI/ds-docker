
#https://technologyconversations.com/2015/07/02/scaling-to-infinity-with-docker-swarm-docker-compose-and-consul-part-14-a-taste-of-what-is-to-come/
#http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html

 curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

 https://clusterhq.com/2015/12/09/difference-docker-volumes-flocker-volumes/


     1  history
    2  docker ps
    3  docker info
    4  docker run hello-world
    5  docker ps
    6  docker ps -a
    7  docker -h
    8  docker ps
    9  docker -H :2333 info
   10  docker -H :2333 ps
   11  docker ps
   12  docker -H :2333 ps run hello-world
   13  docker -H :2333 run hello-world
   14  docker -H :2333 ps
   15  docker -H :2333 ps -a
   16  docker ps -a
   17  hostname
   18  docker -H :2333 ps
   19  docker -H :2333 ps -a
   20  docker -H :2333 run alpine
   21  docker -H :2333 run -it alpine /bin/sh
   22  docker ps
   23  docker images
   24  docker -H :2333 images
   25  docker run -it alpine /binsh
   26  docker -H :2333 images
   27  ls
   28  nano Dockerfile
   29  docker -H :2333 build -t apache_swarm .
   30*  images
   31  docker -H :2333 info
   32  docker -H :2333 images
   33  docker run -d --name apache_swarm_01 -p 80:80 apache_swarm
   34  docker -H : :2333 run -d --name apache_swarm_01 -p 80:80 apache_swarm
   35  docker -H :2333 run -d --name apache_swarm_01 -p 80:80 apache_swarm
   36  docker -H 2333 ps
   37  docker -H :2333 ps
   38  docker -H :2333 info
   39  docker ps
   40  docker -H :2333 run -d --name apache_swarm_02 -p 81:80 apache_swarm
   41  docker -H :2333 ps
   42  docker -H :2333 info
   43  docker -H :2333 run -d --name apache_swarm_03 -p 82:80 apache_swarm
   44  docker -H :2333 info
   45  ip a
   46  ls
   47  docker -H :2333 info
   48  chmod +x /usr/local/bin/docker-compose
   49  ls
   50  docker-compose --version
   51  ls
   52  git
   53  git clone https://github.com/ICESI/distributed-systems.git
   54  ls
   55  cd distributed-systems/mpi/
   56  ls
   57  cd 01_docker_mpi/
   58  ls
   59  cd 01_base_image/
   60  ls
   61  docker -H :2333 build -t openmpi .
   62  docker -H :2333 images
   63  ls
   64  cd ..
   65  ls
   66  cd 02_create_cluster/
   67  ls
   68  docker-compose scale mpi_node=10
   69  docker-compose -H :2333 scale mpi_node=10
   70  docker-compose -H :2333 info
   71  docker -H :2333 info
   72  docker-compose -H :2333 scale mpi_node=1
   73  docker-compose -H :2333 scale mpi_node=100
   74  docker -H :2333 info
   75  docker-compose -H :2333 scale mpi_node=50
   76  docker -H :2333 info
   77  docker-compose -H :2333 scale mpi_node=10
   78  docker-compose -H :2333 scale mpi_node=1
   79  docker-compose -H :2333 scale mpi_node=0
   80  docker -H :2333 info
   81  docker-compose -H :2333 scale mpi_node=5
   82  docker -H :2333 info
   83  history
   84  history > listado