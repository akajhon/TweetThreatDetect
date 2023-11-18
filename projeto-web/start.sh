#!/bin/bash

FILE_NAME="GoogleNews-vectors-negative300.bin.zip"

echo "[+] Descomprimindo o arquivo..."
unzip "$FILE_NAME"

echo "[+] Instalando Dependências..."
pip install -r requirements.txt

echo "[+] Executando Streamlit..."
streamlit run Threat_analysis.py