# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio =  int(input("Digite o valor da sua PA: "))
razão = int(input("Digite o valor da sua razão: "))
fim = int(input("Informe em quantas casa ele vai pular: "))

for pa in range( 1, inicio+1):
    termo = fim + (pa-1) * razão
    print(f"{termo}")
