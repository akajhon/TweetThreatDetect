FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y unzip \
    && apt-get install -y sed \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN chmod +x ./start.sh

ENTRYPOINT ["/bin/bash", "./start.sh"]