def compras():
    try:
        preco1 = float(input("Digite o preço do produto 1: "))
        preco2 = float(input("Digite o preço do produto 2: "))
    except ValueError:
        print("Números por favor")
        return

    total = preco1 + preco2
    print("Valor total da compra: R$ ", total)

compras()