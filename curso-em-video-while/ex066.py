cont = soma = 0 

while True:
    núm = int(input("Digite um valor, caso queira sair digite [999]: "))
    if núm == 999:
     break
    cont +=1
    soma += núm
print(f'A soma dos numero foi de {soma}')
print(f'A quantidade de valores escrito foi de {cont}')
