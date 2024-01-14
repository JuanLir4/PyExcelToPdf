##Essa codigo tranforma xlsx em pdf sem precisar ter o excel instalado na maquina
##por isso as medidas do pdf podem n ficar muito exatas
import pandas as pd
import os
from reportlab.pdfgen import canvas

arquivos = os.listdir('docs')
arquivosunicos2 = []

for arquivo in arquivos:
    caminho_arquivo = os.path.join('docs', arquivo)
    arquivosunicos = pd.read_excel(caminho_arquivo)
    arquivosunicos2.append(arquivosunicos)

ArquivosGerais = pd.concat(arquivosunicos2, ignore_index=True)

pdf_path = "output.pdf"
pdf = canvas.Canvas(pdf_path)

for index, row in ArquivosGerais.iterrows():
    pdf.drawString(100, 800 - index * 20, str(row))

pdf.save()