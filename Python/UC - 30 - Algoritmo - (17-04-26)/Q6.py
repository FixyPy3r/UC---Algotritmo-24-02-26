t = [10, 20, 30, 40, 50, 60, 70]
d = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

soma = 0
for i, temp in enumerate(t):
    print("Dias", {i})
    print("{temp}ºC")
    soma = soma + temp

m = soma / len(t)
print(f"Média da semana: {m:.1f}")