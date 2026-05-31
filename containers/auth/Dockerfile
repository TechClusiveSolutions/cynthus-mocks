FROM debian:bookworm-slim

LABEL maintainer="Jad Wauthier"
LABEL type="base-image"

USER root

WORKDIR /opt/app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-venv curl libidn2-dev libxml2-dev libpq-dev libssl-dev

COPY requirements.txt requirements.txt

RUN mkdir -p /opt/python

RUN python3 -m venv /opt/python

RUN /opt/python/bin/python3 -m pip install -r requirements.txt

EXPOSE 8000/tcp

CMD [ "/opt/app/bin/startup.sh" ]
