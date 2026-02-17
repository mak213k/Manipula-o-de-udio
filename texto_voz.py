import pyttsx3
from pypdf import PdfReader

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

nome_texto = "coloque_o_nome_do_livro_aqui"
pdf_path = nome_texto+".pdf"
arquivo_saida = "livro_final_narracao"

texto = ""

# Extraindo texto do PDF
with open(pdf_path, "rb") as file:
    reader = PdfReader(file)

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            texto += extracted + "\n"

if not texto.strip():
    print("Nenhum texto extraído.")
    exit()

print("Convertendo para áudio...")

# 🔥 Dividir em blocos (fundamental para não travar)
chunk_size = 2500
block = 0

for i in range(0, len(texto), chunk_size):
    chunk = texto[i:i+chunk_size]
    engine.save_to_file(chunk, arquivo_saida+"_"+str(block)+".wav")
    block += 1

engine.runAndWait()
engine.stop()

print("Áudio salvo com sucesso.")