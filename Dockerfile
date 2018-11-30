FROM ubuntu:bionic

MAINTAINER tchoedak <tchoedak@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive
ENV SMTP_USERNAME=$SMTP_USERNAME
ENV SMTP_PASSWORD=$SMTP_PASSWORD

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    vim-tiny \
    build-essential \
    python-dev \
    python3-dev \
    python3.7 \
    python3.7-dev \
    libsasl2-dev \
    python-setuptools \
    python3.7-distutils \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.7 get-pip.py --disable-pip-version-check --no-cache-dir pip setuptools;

RUN python3.7 -m pip install -U pip --no-cache-dir
RUN pip3 install -U pip --no-cache-dir

RUN cp /usr/local/bin/pip3.7 /usr/local/bin/pip
RUN cd /usr/bin && ln -sf python3.7 python3
RUN cd /usr/bin && ln -sf python3.7m python3m

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install virtualenv
RUN virtualenv --python=python3 venv
RUN . venv/bin/activate
RUN pip install -r /tmp/requirements.txt
