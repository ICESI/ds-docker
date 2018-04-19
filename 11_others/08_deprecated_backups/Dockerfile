FROM debian
MAINTAINER daniel.barragan@correo.icesi.edu.co

RUN apt-get update -y && apt-get install python -y
RUN useradd -ms /bin/bash python_user

USER python_user

ADD . /home/python_user
VOLUME /home/python_user
WORKDIR /home/python_user
EXPOSE 8000

CMD ["python","simple_server.py"]
