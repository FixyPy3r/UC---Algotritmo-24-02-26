total = 0.0

while True:
    valor = float(input("Digite o valor, caso queira sair digite 0: "))
    if valor == 0:
        break
    total = total + valor

print(f"Total: R$ {total:.2f}")