#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

numeral = 500
s = 0
for n in range(1, numeral+1):
    if n % 2 == 0:
        continue
    
    if n % 3 == 0:
        s += n
        #print(n)
print(f"A soma de todos os valores é: {s}")

