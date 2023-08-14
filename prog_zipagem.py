import os
from zipfile import ZipFile, ZIP_DEFLATED

def compact(localdoarquivo):
    percorrer_arquivos = os.listdir(localdoarquivo)
    for name in percorrer_arquivos:
        tirandotipo = name.split('.')[0]
        namezip = os.path.join(localdoarquivo, tirandotipo + '.zip')
        archive = ZipFile(namezip, "w", compression=ZIP_DEFLATED)
        archive.write(os.path.join(localdoarquivo, name), name)
        archive.close()

if __name__ == '__main__':
    pastinha = input("Digite o caminho da pasta:")
    compact(pastinha)

