from barcode import EAN13
from barcode.writer import ImageWriter

class Produto:
    def __init__(self, codigo_barra) -> None:
        self.codigo_barra = codigo_barra

    def getcodigoBarras(self):
        codigo_barra = EAN13(self.codigo_barra, writer=ImageWriter())
        return codigo_barra

    def savecodigoBarras(self):
        codigo_barra = self.getcodigoBarras()
        codigo_barra.save("codigo_barras")
        

if __name__ == "__main__":
    p1 = Produto("123568423875")
    p1.savecodigoBarras()




