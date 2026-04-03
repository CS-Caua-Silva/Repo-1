n1 = int(input("Digite um número: "))
n2  = int(input("Digite outro: "))

while True:
    print("Menu\n" \
    "[1] - somar\n" \
    "[2] - multiplicar\n" \
    "[3] - maior\n" \
    "[4] - novos numeros\n" \
    "[5] - sair do progama")
    
    user = input('Digite uma das alternativas (1 - 5): ')
    
        # soma dos valores
    if user == "1":
        soma = n1 + n2
        print(f"O resultado de {n1} + {n2} = {soma}")

        #multiplicação
    elif user == "2":
        multi =  n1*n2
        print(f"{n1} X {n2} = {multi}")

        # maior
    elif user == "3":
       maior = n1 if n1 >= n2 else n2
       print(f"O maior termo é {maior}")

        # Outros números
    elif user == "4":
        n1 = int(input('Digite um novo valor: '))
        n2 =int(input("Outro: "))

        # Sair
    elif user == "5":
        user2 = input("Digite tem certeza que quer sair?\n"" (S/N): ").strip().upper()[0]
        if user2 == "S":
            break
    else:
        print("Opção inválida! Escolha (1 - 5)")
        print("---" * 20)

print("Fim, do progama. Volte sempre!")
