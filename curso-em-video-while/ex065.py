maior = None
menor = None
soma = 0
contador = 0 

while True:

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
        print("Digite um número válido!")

# mostra a média dos números e os resultados
media =  soma / contador
print(f"A média dos termos é: {media}")
if maior is not None:
    print(f"O maior termo é: {maior}")
    print(f"O menor termo é: {menor}")
else:
    print("Nenhum número foi informado!")

# A cima temos uma forma de fazer e a abixo temos outra, as duas foram feitas por mim, so para ver de outra forma de fazer.

'''
resp = 'S'
soma = quant = maior = menor = 0

while  resp in 'Ss':
    num = int(input("Digite um  número: "))
    quant +=1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
media = soma / quant

print('~' * 30)
print(f"A quantidade de termos foi de {quant}")
print(f"A média é {media}")
print(f"O maior valor é {maior}")
'''




