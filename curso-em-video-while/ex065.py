maior = None
menor = None
soma = 0
contador = 0 


while True:
    try:

    # Lê número com tratamento de erro
        numero = int(input("Informe um número: "))
        soma += numero
        contador += 1
        pergunta = input("Deseja continuar? (S/N): ").strip().upper()

    # Atualiza maior/menor
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        
     # Verifica resposta
        if pergunta == "N":
            break
    except ValueError:
        print("Digite um número válido!")

# mostra a média dos números e os resultados
media =  soma / contador
print(f"A média dos termos é: {media}")
if maior is not None:
    print(f"O maior termo é: {maior}")
    print(f"O menor termo é: {menor}")
else:
    print("Nenhum número foi informado!")