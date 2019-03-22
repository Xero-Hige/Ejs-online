FROM debian:testing

MAINTAINER TuNick <TuMail>
WORKDIR /

RUN apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends \
    build-essential \
	python3 \
	python3-pip \
	python3-setuptools && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    mkdir /server

RUN pip3 install wheel --no-cache-dir && \
    pip3 install flask --no-cache-dir && \
    pip3 install flask-cors --no-cache-dir && \
    pip3 install gunicorn --no-cache-dir && \
    pip3 install Flask-WTF  --no-cache-dir


WORKDIR /server

CMD ["gunicorn","--bind","0.0.0.0:8000","app:app"]