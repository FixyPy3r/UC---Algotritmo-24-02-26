notas = [8.5, 6.0, 9.2, 5.5, 7.8]

q = 0
for nota in notas:
    if nota > 7:
        q = q + 1

print(f"Notas maior que 7: {q}")