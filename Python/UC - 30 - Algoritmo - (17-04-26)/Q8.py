valor = float(input("Valor da compra: R$ "))

if valor > 500:
    d = 0.20
elif valor >= 200:
    d = 0.10
else:
    d = 0

pfl = valor * (1 - d)
print(f"Desconto: {int(d*100)}%")
print(f"Preço: R$ {pfl:.2f}")