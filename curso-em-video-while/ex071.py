print('-' * 30 )
print('BANCO Y')
print('-' * 30)

saque = int(input('Qual valor você deseja sacar? R$ '))
total = saque
contador_cedulas = 0
ced = 100

while True:
    if total >= ced:
        total -= ced
        contador_cedulas += 1
    else:
        if contador_cedulas > 0:
            print(f'Foi ultilizado cédulas de R${ced} em {contador_cedulas} vezes.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1

        contador_cedulas = 0

        if total == 0:
            break
print('=' * 30)

print('Volte sempre ao BANCO Y! Tenha um bom dia!')




