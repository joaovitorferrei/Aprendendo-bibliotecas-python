from Clases.codbarras.gerador_codebarras import Produto
if __name__ == "__main__":
    produtos = []
    while True:
        codigo_barra = input("Digite o código de barras do produto (ou digite 'sair' para encerrar): ")
        if codigo_barra.lower() == 'sair':
            break
        p = Produto(codigo_barra)
        p.savecodigoBarras()
        produtos.append(p)

    for produto in produtos:
        dicionario = produto.criar_dicionario()
        print("Dicionário de produtos:", dicionario)
