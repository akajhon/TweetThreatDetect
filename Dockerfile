FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y unzip \
    && apt-get install -y sed \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN chmod +x ./start.sh

RUN pip install -r ./requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m spacy download en_core_web_sm

ENTRYPOINT ["/bin/bash", "./start.sh"]
