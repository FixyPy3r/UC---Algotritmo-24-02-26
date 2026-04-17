vendas = [1, 2, 3, 4, 5, 8, 10]

sp = 0
for v in vendas:
    if v % 2 == 0:
        sp = sp + v

print(f"Soma dos valores pares: R$ {sp}")