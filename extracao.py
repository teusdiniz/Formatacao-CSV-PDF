import os
import pytesseract
from pdf2image import convert_from_path
import pandas as pd
import re
import fitz
from tqdm import tqdm

# === CONFIGURAÇÕES ===
pdf_path = "C:/Users/mathe/Desktop/Faculdade/merged.pdf"
poppler_path = r"C:\poppler\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\\tessdata"

# === CONTAR TOTAL DE PÁGINAS ===
total_paginas = len(fitz.open(pdf_path))

# === LISTA PARA DADOS EXTRAÍDOS ===
dados_extraidos = []
unidade_atual = ""

print("🔄 Processando páginas do PDF...")

for i in tqdm(range(total_paginas), desc="📄 Página", unit="pág"):
    try:
        imagem = convert_from_path(
            pdf_path,
            poppler_path=poppler_path,
            dpi=150,
            first_page=i + 1,
            last_page=i + 1
        )[0]

        texto = pytesseract.image_to_string(imagem)
        linhas = texto.splitlines()

        for idx, linha in enumerate(linhas):
            linha = linha.strip()

            # 🔍 DETECÇÃO FLEXÍVEL DO CABEÇALHO
            if "RELACAO DE MATERIAL PERMANENTE" in linha.upper() or "RELAÇÃO DE MATERIAL PERMANENTE" in linha.upper():
                for j in range(idx + 1, len(linhas)):
                    proxima = linhas[j].strip()
                    if proxima:  # linha não vazia
                        unidade_atual = proxima
                        print(f"✅ Página {i+1} - Unidade capturada: {unidade_atual}")
                        break
                continue

            # 🔍 DETECÇÃO DE LINHA DE MATERIAL
            if re.match(r"\d{3}\.\d{3}\.\d{3}", linha):
                try:
                    partes = linha.split()
                    classif = partes[0]
                    chapa = partes[1]

                    # Extrair data
                    data_match = re.search(r"\d{2}/\d{2}/\d{4}", linha)
                    if not data_match:
                        continue
                    atualiz = data_match.group()

                    # Valor final
                    valor_raw = partes[-1]
                    valor = float(valor_raw.replace(".", "").replace(",", "."))

                    # Descrição entre chapa e data
                    linha_pos_chapa = linha.split(chapa, 1)[1]
                    descricao = linha_pos_chapa.split(atualiz)[0].strip()

                    # Salvar com unidade atual
                    dados_extraidos.append((classif, chapa, descricao, atualiz, valor, unidade_atual))
                    print(f"➕ {classif} | {chapa} | {descricao} | {atualiz} | {valor} | {unidade_atual}")
                except Exception as e:
                    print(f"⚠️ Erro na linha da página {i+1}: {linha}")
    except Exception as erro:
        print(f"❌ Erro ao processar página {i+1}: {erro}")

# === SALVAR NO EXCEL ===
df = pd.DataFrame(dados_extraidos, columns=["CLASSIF", "CHAPA", "DESCRICAO", "ATUALIZ", "VL_ATUAL", "UNIDADE"])
output_path = "C:/Users/mathe/Desktop/Faculdade/materiais_final_ok.xlsx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_excel(output_path, index=False)

print(f"\n✅ Arquivo Excel gerado com sucesso: {output_path}")