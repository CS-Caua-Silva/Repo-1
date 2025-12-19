# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

numero = int(input("Digite um numero: "))
print(f"Aqui esta todo os numero pares:")
for c in range(1, numero+1):
    if c % 2 == 1:
        continue
    print(c)
