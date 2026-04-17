frase = input("Digite uma frase: ")
vogal = "a, e, i, o, u"

contagem = 0
for letra in frase.lower():
    if letra in vogal:
        contagem = contagem + 1

print(f"Total das vogais: {contagem}")