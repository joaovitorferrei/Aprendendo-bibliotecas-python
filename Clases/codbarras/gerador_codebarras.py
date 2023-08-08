from barcode import EAN13
from barcode.writer import ImageWriter
import os

class Produto:
    def __init__(self, codigo_barra) -> None:
        self.codigo_barra = codigo_barra

    def getcodigoBarras(self):
        codigo_barra = EAN13(self.codigo_barra, writer=ImageWriter())
        return codigo_barra

    def savecodigoBarras(self):
        codigo_barra = self.getcodigoBarras()
        filename = f"codigo_barras_{self.codigo_barra}"
        save_dir = os.path.join(os.getcwd(), "img")
        os.makedirs(save_dir, exist_ok=True)
        full_path = os.path.join(save_dir, filename)
        codigo_barra.save(full_path)
    
    def criar_dicionario(self):
        dicionario = {}
        while True:
            try:
                chave = input("Digite o nome do produto (ou digite 'sair' para encerrar): ")
                if chave.lower() == 'sair':
                    break
                valor = float(input("Digite o valor correspondente: "))
                dicionario[chave] = valor
            except ValueError:
                print("Erro: Valor inválido. Digite um número para o valor.")
        return dicionario











