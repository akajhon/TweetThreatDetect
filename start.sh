#!/bin/bash

# Variables
ZIP_FILE="GoogleNews-vectors-negative300.bin.gz"
EXTRACTED_FILE="./models/GoogleNews-vectors-negative300.bin"

if [ ! -f "$EXTRACTED_FILE" ]; then
    echo "[+] Arquivo $EXTRACTED_FILE não encontrado. Baixando e descomprimindo o arquivo..."
    wget "https://figshare.com/ndownloader/files/41403483" -O $ZIP_FILE
    gunzip -c $ZIP_FILE > $EXTRACTED_FILE
else
    echo "[+] Arquivo $EXTRACTED_FILE já foi extraído."
fi

echo "[+] Removendo arquivo .gz..."
rm -rf ./models/GoogleNews-vectors-negative300.bin.gz

echo "[+] Instalando Dependências..."
pip install -r requirements.txt

echo "[+] Baixando o pacote punkt..."
python3 -m nltk.downloader punkt

echo "[+] Baixando o pacote wordnet..."
python3 -m nltk.downloader wordnet

echo "[+] Baixando o pacote stopwords..."
python3 -m nltk.downloader stopwords

echo "[+] Baixando o pacote en_core_web_sm..."
python3 -m spacy download en_core_web_sm

echo "[+] Executando Streamlit..."
streamlit run Main.py
