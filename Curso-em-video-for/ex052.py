#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um numero: "))
# primerio teste para verificar se a string  é numero primo
if numero < 2: # A qui eu peço para ver se ele é maior que 2
    print("Seu numero não é primo") 
else:
    primo = True # caso seja maior, eu atribuo que o primo é verdade

    for verifica_SeE_numero_primo in range(2, int( numero ** 0.5)+ 1):
        if  numero % verifica_SeE_numero_primo == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")