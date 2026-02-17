# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio =  int(input("Digite o valor da sua PA: "))
razão = int(input("Digite o valor da sua razão: "))
quantidade = int(input("Informe a quantidade de termos: "))

for pa in range( 1, quantidade+1):
    termo = inicio + (pa-1) * razão
    print(f"{termo}")
