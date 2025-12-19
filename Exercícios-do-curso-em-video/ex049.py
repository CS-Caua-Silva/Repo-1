# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero_da_tabuada = int(input("Digite o número que deseja ver a tabuada: "))
for tabuada in range(1,11):
    multiplicar = tabuada * numero_da_tabuada
    print(f"{tabuada} X {numero_da_tabuada} = {multiplicar}")

