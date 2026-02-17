user = cont = soma = 0
user = int(input("Digite um termo, Caso não quira digite (999): "))
while user != 999:
    cont += 1
    soma += user
    user = int(input("Digite um termo, Caso não quira digite (999): "))
print(f"Total de números: {cont}")
print(f'O total da soma dos termo é {soma}')
