FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y gunzip \
    && apt-get install -y sed \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN chmod +x ./start.sh

COPY ./corpora /root/nltk_data/corpora
COPY ./tokenizers /root/nltk_data/tokenizers

ENTRYPOINT ["/bin/bash", "./start.sh"]
