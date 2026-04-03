

while True:  

    print('~' * 40)
    num = float(input('Quer ver a tubuada de qual valro? '))
    print('~' * 40)

    if num  < 0:
        print('Você digitou um valor negativo! O progama foi finalizado')
        break

    cont = 1
    while cont <= 10:
        resultado = cont * num
        print(f'{cont} x {num:.0f} = {resultado:.0f}')
        cont += 1

print('~' * 40)
        