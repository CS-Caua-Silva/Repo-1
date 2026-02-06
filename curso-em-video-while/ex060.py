fatorial = 1
número = int(input("Digite um valor: "))
contador = número

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"{número}! = {fatorial}")