FROM centos:7

LABEL author="Daniel Barragan"
LABEL image_name="base_builder"
LABEL description="container with builder dependencies"

ENV LC_ALL=en_US.utf8
ENV LANG=en_US.utf8

RUN yum install https://centos7.iuscommunity.org/ius-release.rpm -y
RUN yum install rpm-build python36u python36u-pip -y
RUN yum install git -y
