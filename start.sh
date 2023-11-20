#!/bin/bash

ZIP_FILE="GoogleNews-vectors-negative300.zip"
EXTRACTED_FILE="./models/GoogleNews-vectors-negative300.bin"
PATH_IN_ZIP="GoogleNews-vectors-negative300.bin"

if [ ! -f "$EXTRACTED_FILE" ]; then
    echo "[+] Arquivo $EXTRACTED_FILE não encontrado. Descomprimindo o arquivo..."
    unzip -j "$ZIP_FILE" "$PATH_IN_ZIP" -d "./models"
else
    echo "[+] Arquivo $EXTRACTED_FILE já foi extraído."
fi

echo "[+] Instalando Dependências..."
pip install -r requirements.txt

echo "[+] Baixando o pacote en_core_web_sm..."
python -m spacy download en_core_web_sm

echo "[+] Executando Streamlit..."
streamlit run Main.py