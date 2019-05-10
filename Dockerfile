FROM alpine:latest

MAINTAINER Florencia97 <florrr1997@gmail.com>
WORKDIR /

RUN apk add --update \
    python3 && \
#	python3 &&\
#	python3-pip \
#	python3-setuptools && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /src

WORKDIR /src
