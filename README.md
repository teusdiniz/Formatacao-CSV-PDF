# 📄 Extração Automatizada de Dados de PDF Escaneado com OCR

Este projeto tem como objetivo automatizar a extração de dados estruturados a partir de documentos PDF escaneados com centenas de páginas. A solução foi aplicada para processar um arquivo com mais de **700 páginas**, gerando um **CSV com mais de 27.000 linhas** de dados limpos, organizados e prontos para análise.

## 🚀 Funcionalidades

- Conversão de páginas de PDF em imagens com `pdf2image`
- Reconhecimento de texto com OCR utilizando `pytesseract`
- Extração de campos: classificação, chapa, descrição, data e valor
- Detecção automática da unidade administrativa associada a cada item
- Validação e limpeza de dados
- Exportação para arquivo `.xlsx` (Excel) e `.csv`

## 🧰 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [pdf2image](https://pypi.org/project/pdf2image/)
- [pandas](https://pypi.org/project/pandas/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [tqdm](https://tqdm.github.io/)
- Tesseract OCR
- Poppler (para Windows)

## 📂 Estrutura do Projeto

📁 extrator_pdf_ocr/
┣ 📄 extrator.py → Script principal
┣ 📄 requirements.txt → Dependências do projeto
┣ 📄 README.md → Este arquivo
┣ 📂 data/
┃ ┗ 📄 merged1.pdf → PDF original escaneado (não incluído)
┗ 📂 output/
┗ 📄 materiais_final.xlsx → Arquivo gerado com os dados extraídos

markdown
Copiar
Editar

## ⚙️ Requisitos

- Python 3.8 ou superior
- Tesseract OCR instalado ([Download](https://github.com/tesseract-ocr/tesseract))
- Poppler for Windows ([Download](http://blog.alivate.com.au/poppler-windows/))

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seunome/extrator-pdf-ocr.git
cd extrator-pdf-ocr
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Verifique se o Tesseract e o Poppler estão corretamente instalados e configurados no seu sistema (PATH).

▶️ Execução
bash
Copiar
Editar
python extrator.py
O script irá ler o arquivo PDF configurado no caminho pdf_path, extrair as informações e gerar uma planilha com todos os dados organizados.

✅ Resultado
Arquivo Excel com os dados estruturados por unidade

Mais de 27 mil linhas extraídas automaticamente

Ideal para automatizar registros patrimoniais, documentos públicos e outros tipos de listagens escaneadas

🧠 Lições Aprendidas
Como lidar com PDFs escaneados de baixa qualidade

Estratégias para detectar blocos de dados e cabeçalhos com OCR ruidoso

Otimizações para leitura em lote e tratamento de exceções

📷 Exemplo de Funcionamento

📩 Contato
Caso queira adaptar essa solução para sua realidade ou tenha dúvidas, entre em contato comigo pelo LinkedIn ou abra uma Issue!
