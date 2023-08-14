from zipfile import ZipFile

with ZipFile("arquivo_compactado2.zip", "w") as zipagem:
    zipagem.write("imagens\Ornn_0.jpg")

with ZipFile("arquivo_compactado2.zip", "r") as zipagem:
    zipagem.extractall("destino")
