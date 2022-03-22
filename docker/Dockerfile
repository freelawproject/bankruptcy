FROM python:3.10-slim

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install nginx -y
RUN apt-get install git -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY bankruptcy-docker /opt/app/bankruptcy-docker
COPY manage.py /opt/app/
WORKDIR /opt/app

COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 5050
COPY docker/docker-entrypoint.sh /opt/app/
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]
ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]
