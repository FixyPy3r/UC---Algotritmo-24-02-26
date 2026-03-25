def cal():
    sair = False

    while sair == False:
        print("Calcule")
        print("1 soma")
        print("2 subtração")
        print("3 multiplicação")
        print("4 divisão")
        print("5 sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Tchau")
            sair = True

        else:
            n1 = float(input("Digite o um numero: "))
            n2 = float(input("Digite outro número: "))

            if opcao == "1":
                resultado = n1 + n2
                print("Resultado:", resultado)

            elif opcao == "2":
                resultado = n1 - n2
                print("Resultado:", resultado)

            elif opcao == "3":
                resultado = n1 * n2
                print("Resultado:", resultado)

            elif opcao == "4":
                if n2 != 0:
                    resultado = n1 / n2
                    print("Resultado:", resultado)
                else:
                    print("Imbecil!")

            else:
                print("Opção inválida!")