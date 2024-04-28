# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        gzip \
        sed \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make start script executable
RUN chmod +x ./start.sh

# Copy NLTK data
COPY ./corpora /root/nltk_data/corpora
COPY ./tokenizers /root/nltk_data/tokenizers

# Define environment variable
ENV NLTK_DATA /root/nltk_data

# Run start.sh when the container launches
ENTRYPOINT ["/bin/bash", "./start.sh"]
