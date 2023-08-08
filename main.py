from Clases.codbarras.gerador_codebarras import Produto,codigos_produtos
if __name__ == "__main__":
    for produto_nome, codigo_barra in codigos_produtos.items():
        produto = Produto(codigo_barra)
        produto.savecodigoBarras()