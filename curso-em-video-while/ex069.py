contador_idade = 0
contador_homens = 0
contador_mulheres_menos_20 = 0

print(' ---- CADASTRAR PESSOAS ----')

while True:

  # Verificar o Sexo
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
        sexo = sexo[0]
        
        if sexo == '':
            continue
        if sexo in ['M', 'F']:
            break

  # Verificar a Idade
    while True:
        idade_str = input('Qual seria a idade? ')

        if idade_str == '':
            continue
        if idade_str.isdigit():
            idade = int(idade_str)
            break

    print('-' * 30)
  # Verificar os contadores
    if sexo == 'M':
        contador_homens += 1
    
    if sexo == 'F':
        if idade < 20:
            contador_mulheres_menos_20 += 1
    if idade > 18:
        contador_idade += 1

  # Verificar continuar
    while True:
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()
        continuar = continuar[0]

        if continuar == '':
            continue
        elif continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            continue

    if continuar == 'N':
        break

print('-' * 30)
print(' ==== RESILTADO ===')
print(f'O total de pessoas que tem mais de 18 anos é: {contador_idade}')
print(f'O total de homens é de {contador_homens}')
print(f'O total de mulheres abaixo de 20 anos é {contador_mulheres_menos_20}')



'''
Aqui foi o exercio feito na video aula, acima foi feito por mim.

tot18 = 0
totH = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou!')
print(f'O total de pessoas com mais de 18 anos {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos')
'''

