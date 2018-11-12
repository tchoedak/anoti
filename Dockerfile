FROM ubuntu:bionic

MAINTAINER tchoedak <tchoedak@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    python-pip \
    libmysqlclient-dev \
    netcat \
    vim-tiny \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    build-essential \
    python-dev \
    python3-dev \
    libsasl2-dev \
    python-setuptools \
    python3-pip \
    python3-setuptools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install -U pip --no-cache-dir
RUN pip3 install -U pip --no-cache-dir
RUN pip2 install -U pip --no-cache-dir

RUN cp /usr/local/bin/pip2.7 /usr/local/bin/pip
ADD requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt \
    --no-cache-dir
