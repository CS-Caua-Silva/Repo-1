# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
for numeros in range(0, 6):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 1:
        continue
    s += valor
print(s)

