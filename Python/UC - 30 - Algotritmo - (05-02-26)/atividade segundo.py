import random

numeros = [91, 34, 67, 15, 82]

print("Lista original: ", numeros)
numeros.sort()
print("Após Crescente: ", numeros)
numeros.sort(reverse=True)
print("Após Decrescente: ", numeros)


numeros2 = [80, 7, 10, 9, 19]

random.shuffle(numeros2)
print("Aleatório: ",  numeros2)

# Desafio pra encher o saco

numeros3 = [1, 2, 3, 4, 5, 6]

print("Crescente: ", numeros3)
numeros3.sort(reverse=True)
print("Decrescente: ", numeros3)

random.shuffle(numeros3)
print("Aleatório: ",  numeros3)
