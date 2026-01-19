import os
import re
import pdfplumber
import pytesseract

PASTA = "notas"

def extrair_dados(pdf_path):
    texto = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            img = page.to_image(resolution=300).original
            texto += pytesseract.image_to_string(img, lang="por") + "\n"

    # Número da nota
    nota_match = re.search(r"Número da nota\s*(\d+)", texto, re.IGNORECASE)

    # Razão Social
    razao_match = re.search(r"Nome/Raz[aã]o social:\s*(.+)", texto, re.IGNORECASE)

    numero = nota_match.group(1) if nota_match else "SEM_NUMERO"
    razao = razao_match.group(1).strip() if razao_match else "SEM_RAZAO"

    razao = re.sub(r'[\\/*?:"<>|]', '', razao)  # limpa caracteres inválidos

    return numero, razao

for arquivo in os.listdir(PASTA):
    if arquivo.lower().endswith(".pdf"):
        caminho = os.path.join(PASTA, arquivo)

        numero, razao = extrair_dados(caminho)

        novo_nome = f"NFSE N {numero} {razao}.pdf"
        novo_caminho = os.path.join(PASTA, novo_nome)

        os.rename(caminho, novo_caminho)
        print(f"Renomeado: {arquivo} → {novo_nome}")
