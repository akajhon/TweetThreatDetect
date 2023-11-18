#!/bin/bash

ZIP_FILE="GoogleNews-vectors-negative300.bin.zip"
EXTRACTED_FILE="./GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin"

if [ ! -f "$EXTRACTED_FILE" ]; then
    echo "[+] Arquivo $EXTRACTED_FILE não encontrado. Descomprimindo o arquivo..."
    unzip "$ZIP_FILE"
else
    echo "[+] Arquivo $EXTRACTED_FILE já foi extraído."
fi

echo "[+] Instalando Dependências..."
pip install -r requirements.txt

echo "[+] Executando Streamlit..."
streamlit run Threat_analysis.py