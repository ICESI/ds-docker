FROM ubuntu
MAINTAINER daniel.barragan@correo.icesi.edu.co

RUN apt update
RUN apt install python -y
RUN apt install wget -y
RUN wget https://bootstrap.pypa.io/get-pip.py -P /tmp
RUN python /tmp/get-pip.py
RUN pip install flask

# CMD ["/bin/bash"]
CMD ["/usr/bin/python","/tmp/microservice_a.py"]
