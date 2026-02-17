'''from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial
print(f"O fatorial de {n} é {f}")'''

número = int(input("Digite um valor: "))
contador = número
fatorial = 1

print(f"Calculando {número}! = ", end='')
while contador > 0:
    print(f"{contador} ", end='')
    print("x " if contador > 1 else " = ", end='')
    fatorial *= contador
    contador = contador - 1
print(f"{fatorial}")
