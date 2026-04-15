def media():
    try:
        nota1 = float(input("Nota 1 em NÚMEROS: "))
        nota2 = float(input("Nota 2 em NÚMEROS: "))
        nota3 = float(input("Nota 3 em NÚMEROS: "))
    
    except ValueError:
        print("Coloque números:")
        return
    
    media = nota1 + nota2 + nota3 /3
    print("Sua média final vai ser", media)

media()