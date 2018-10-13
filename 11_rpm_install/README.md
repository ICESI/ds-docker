### Docker Flow 

#### Container for building artifacts
```
FROM centos:7
LABEL author="Daniel Barragan"
LABEL image_name="icesi_builder"
LABEL description="Builder Image"

RUN yum install https://centos7.iuscommunity.org/ius-release.rpm -y
RUN yum install rpm-build python36u python36u-pip -y
```

Simple test with container creation and artifact building
```
docker build -t icesi_builder:0.1.0 .
docker run -it --rm icesi_builder:0.1.0 
# cd /root/
# git clone https://github.com/ICESI/so-microservices-python-part2.git
# cd so-microservices-python-part2/05_artifacts/
# python3.6 setup.py bdist_rpm --requires="python36u python36u-pip" --post-install="scripts/post_install_py3.sh" --python=/usr/bin/python3.6 
```

#### Container base for services
```
FROM centos:7
LABEL author="Daniel Barragan"
LABEL image_name="icesi_base"
LABEL description="Base Image for Icesi Services"

RUN yum install https://centos7.iuscommunity.org/ius-release.rpm -y
```

Simple test with container creation
```
docker build -t icesi_base:0.1.0 .
docker run -it --rm icesi_base:0.1.0
```

#### Container service (Just for testing)
```
FROM icesi_base:0.1.0

ENV LC_ALL=en_US.utf8
ENV LANG=en_US.utf8 

COPY so-microservices-python-part2/05_artifacts/dist /root/
WORKDIR /root/
RUN yum install gm_analytics-0.1.0.dev20181012-1.noarch.rpm -y

CMD ["connexion", "run", "/usr/lib/python3.6/site-packages/gm_analytics/swagger/indexer.yaml", "--verbose"]
```

Simple test with container creation
```
docker build -t icesi_service:0.1.0 .
docker run -d -p 5000:5000 --name icesi_service icesi_service:0.1.0
docker logs icesi_service -f
```
