FROM ubuntu
MAINTAINER daniel.barragan@correo.icesi.edu.co

RUN apt update -y && \
  apt install python -y && \
  apt install wget -y

RUN wget https://bootstrap.pypa.io/get-pip.py -P /tmp && \
  python /tmp/get-pip.py && \
  pip install flask

ADD sources /tmp

CMD ["/usr/bin/python","/tmp/microservice_a.py"]
