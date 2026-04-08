def controle_financeiro(mesada, gastos):
 
    gastot = 0
 
    for gasto in gastos:
        gastot = gastot + gasto
 
    if gastot <= mesada:
        economia = mesada - gastot
        print("Voce gastou R$", gastot, "e sua mesada era R$", mesada)
        print("Voce economizou R$", economia, "esse mes! Parabens!")
    else:
        faltou = gastot - mesada
        print("Voce gastou R$", gastot, "e sua mesada era R$", mesada)
        print("Voce gastou R$", faltou, "a mais do que tinha. Cuidado!")
 
gastosdj = [150, 80, 60, 40, 90]
mesadadj = 500
 
controle_financeiro(mesadadj, gastosdj)