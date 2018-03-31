### Introducción a la virtualización con contenedores virtuales

Universidad ICESI  
Curso: Sistemas Distribuidos  
Docente: Daniel Barragán C.  
Tema: Introducción a la virtualización con contenedores virtuales  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Emplear contenedores virtuales para tareas específicas

### Guía
Descargar la imagen de docker networkboot/dhcpd y crear un contenedor con los parámetros
que se indican a continuación
```
docker pull networkboot/dhcpd
mkdir data
vi data/dhcpd.conf
docker run -it --rm --net=host -v "$(pwd)/data":/data networkboot/dhcpd eno1
```

Crear una sub-interface en el sistema operativo anfitrión y una máquina virtual por medio de vagrant
como se indica a continuación
```
sudo ip addr add 192.168.131.1/24 dev eno1:0
vagrant init centos7
vi Vagrantfile
config.vm.network "public_network", bridge: "eno1"
vagrant up
```

Verifique que la máquina virtual creada con vagrant recibe una dirección IP del contenedor.

### Referencias
https://hub.docker.com/r/networkboot/dhcpd/
