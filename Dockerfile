FROM centos

RUN yum -y install python36
RUN ln -s /usr/bin/python3.6 /usr/local/bin/python
RUN yum -y install java-1.8.0-openjdk

ENV JAVA_HOME /usr/lib/jvm/jre
