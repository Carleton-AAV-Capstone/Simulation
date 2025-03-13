FROM carlasim/carla:0.9.13

USER root

RUN apt-get update && \
    apt-get install -y python3-pip
RUN pip3 install --upgrade pip

RUN pip3 install --upgrade pip
RUN pip3 install --user pygame numpy
RUN pip3 install carla

COPY carla_scripts carla_scripts

