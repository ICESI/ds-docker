```
docker pull networkboot/dhcpd
mkdir data
vi data/dhcpd.conf
docker run -it --rm --net=host -v "$(pwd)/data":/data networkboot/dhcpd en01
```

```
sudo ip addr add 192.168.131.1/24 dev eno1:0
vagrant init centos7
vi Vagrantfile
config.vm.network "public_network", bridge: "eno1"
vagrant up
```
