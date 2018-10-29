FROM icesi_builder:0.1.0

LABEL author="daniel.barragan"
LABEL description="container for creating artifacts"

RUN git clone -b d4n13lbc/artifacts https://github.com/ICESI-Training/sd2018b-workshop2.git /tmp/sd2018b-workshop2

WORKDIR /tmp/sd2018b-workshop2
RUN python3.6 setup.py bdist_rpm --post-install="scripts/post_install_py3.sh" --python="/usr/bin/python3.6"

WORKDIR /tmp/sd2018b-workshop2/dist
RUN yum --nogpgcheck localinstall gm_analytics-*.noarch.rpm -y

