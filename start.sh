#!/bin/bash

# Variables
FILEID="1QZ9OIr0vWYJDYThMBaY76UJcqWwIjHFP"
ZIP_FILE="GoogleNews-vectors-negative300.zip"
EXTRACTED_FILE="./models/GoogleNews-vectors-negative300.bin"
PATH_IN_ZIP="GoogleNews-vectors-negative300.bin"
CONFIRM_TOKEN=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$FILEID" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')

if [ ! -f "$EXTRACTED_FILE" ]; then
    echo "[+] Arquivo $EXTRACTED_FILE não encontrado.  Baixando e Descomprimindo o arquivo..."
    wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$CONFIRM_TOKEN&id=$FILEID" -O $ZIP_FILE && rm -rf /tmp/cookies.txt
    unzip -j "$ZIP_FILE" "$PATH_IN_ZIP" -d "./models"
else
    echo "[+] Arquivo $EXTRACTED_FILE já foi extraído."
fi

echo "[+] Removendo arquivo .zip..."
rm -rf ./GoogleNews-vectors-negative300.zip

echo "[+] Instalando Dependências..."
pip install -r requirements.txt

echo "[+] Baixando o pacote en_core_web_sm..."
python3 -m spacy download en_core_web_sm

echo "[+] Executando Streamlit..."
streamlit run Main.py