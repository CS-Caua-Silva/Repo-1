user = int(input("Digite um valor: "))
contador = 1

while True:
    user = int(input("Deseja escrever mais um termo? Caso não quira digite (999): "))
    if user == 999:
        break
    if user != 999:
        contador += 1
        continue
print(f"Total de números: {contador}")





