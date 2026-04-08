N = int(input("Qual o número de pessoas infectads no primeiro dia "))
R = int(input("Fator Reprodutivo "))
P = int(input("Número de pessoas alvo da infecção "))

dias = 0
infectados_hoje = N
total_infectados = N

while total_infectados < P:
    infectados_amanha = infectados_hoje * R
    total_infectados = total_infectados + infectados_amanha
    infectados_hoje = infectados_amanha
    dias = dias + 1

print("Dias decorridos", dias)