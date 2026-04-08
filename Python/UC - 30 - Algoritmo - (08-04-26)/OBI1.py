Pao = int(input())
Doce = int(input())
Bolo = int(input())

total = Pao * 1 + Doce * 2 + Bolo * 3

if total >= 150:
    print("Bolo")
elif total >= 120:
    print("Doce")
elif total >= 100:
    print("Pao")
else:
    print("N")
