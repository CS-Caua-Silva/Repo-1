# apenas um teste 

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''valor = 1
while valor != 0:
    valor = int(input('Digite um valor: '))
    print(valor)
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] : ')).upper()
print("Fim")'''

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0: # números páres
            par += 1
        if n % 2 == 1: # números ímpares
            impar += 1
print(f"O número total de pares é: {par}")
print(f"O número total de ímpares é: {impar}")

