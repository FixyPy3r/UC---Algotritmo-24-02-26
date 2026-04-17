def calcularimc(p, a):
    imc = p / (a ** 2)
    if imc < 24.9:
        categoria = "Magro"
    else:
        categoria = "Acima do peso"
    return imc, categoria

try:
    p  = float(input("Peso em kg: "))
    a = float(input("Altura em metros: "))
    imc, cat = calcularimc(p, a)
    print(f"IMC: {imc:.1f} — {cat}")
except ValueError:
    print("Coloque números")
except ZeroDivisionError:
    print("Você deveria estudar mais matemática")