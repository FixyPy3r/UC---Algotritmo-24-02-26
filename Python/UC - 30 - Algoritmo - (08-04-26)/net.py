def uso_de_internet(consumod):
 
    limite = 30
 
    total = 0
 
    for consumo in consumod:
        total = total + consumo
 
    print("Total consumido:", total, "GB")
    print("Limite do plano:", limite, "GB")
 
    if total <= limite:
        sobrou = limite - total
        print("Voce ainda tem", sobrou, "GB disponivel no plano, parabens!")
    else:
        passou = total - limite
        print("Voce ultrapassou o limite em", passou, "GB! muito burro!")

consumo_do_lucas = [1.5, 2.0, 0.8, 3.2, 1.0, 2.5, 1.8, 4.0, 0.5, 2.2]
 
uso_de_internet(consumo_do_lucas)