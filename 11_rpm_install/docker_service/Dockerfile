FROM centos

LABEL author="daniel.barragan"
LABEL description="Artifacts maker"

RUN yum install git -y
#RUN git clone https://github.com/ICESI/so-microservices-python-part2.git /root/gm_analytics

ADD so-microservices-python-part2 /root/
RUN yum --nogpgcheck localinstall gm_analytics-0.1.0.dev20181010-1.noarch.rpm

# In progress ...
