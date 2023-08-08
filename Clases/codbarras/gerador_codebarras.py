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
    
codigos_produtos = {
    "açai": "332564812459",
    "arroz": "156845239452",
    "feijão": "482345612586",
    "macarão": "456123889425",
    "peixe":"158346589425"
}  








