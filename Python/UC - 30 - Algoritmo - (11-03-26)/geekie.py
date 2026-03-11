aluno = {}

aluno["nome"] = input("Qual o seu nome: ")
aluno["nota1"] = int(input("Qual sua nota da prova 1: "))
aluno["nota2"] = float(input("Qual sua nota da prova 2: "))

media = (aluno["nota1"] + aluno["nota2"]) /2

aluno["media"] = media

print("\n Dados")
print("Nome: ", aluno["nome"])
print("Primeira nota: ", aluno["nota1"])
print("Segunda nota: ", aluno["nota2"])
print("Média: ", aluno["media"])

if aluno["media"] >= 7:
    print("Você está aprovado")

if aluno["media"] <= 5:
    print("Reprovado")