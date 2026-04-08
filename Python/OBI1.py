Pao = int(input())
Doce = int(input())
Bolo = int(input())

total = Pao * 1 + Doce * 2 + Bolo * 3

if total >= 150:
    print("B")
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")