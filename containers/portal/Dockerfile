FROM ghcr.io/techclusivesolutions/cynthus-base:main

USER root

WORKDIR /opt/app

RUN apt-get update
RUN apt-get upgrade -y

COPY requirements.txt requirements.txt

run /opt/python/bin/python3 -m pip install -r requirements.txt

EXPOSE 8000/tcp

CMD [ "/opt/app/bin/startup.sh" ]
