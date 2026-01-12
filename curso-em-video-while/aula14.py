n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        par +=1
    else:
        impar += 1

print(f"O total de numeros pares é {par} e o total de impares é de {impar}")



