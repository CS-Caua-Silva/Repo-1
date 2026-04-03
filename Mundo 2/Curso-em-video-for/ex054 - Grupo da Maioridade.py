#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date #bliblioteca

hoje = date.today()
ano_hoje = hoje.year

print(F"A data de hoje é {hoje}")
maior_idade = 0
menor_idade = 0

quantidade = int(input("Quantas pessoas deseja cadastrar? "))


for pessoas in range(1, quantidade+1):
    print('-=-' * 30)
    nascimento = input(f"Digite a data de nascimento da pessoa {pessoas}: ").strip()
    print('-=-' * 30)
    for sep in ['-', ' ','|','.']:
        nascimento = nascimento.replace(sep, '/')

    data_com_barra = nascimento.split('/')

    if len(data_com_barra) >= 3:
        ano_str = data_com_barra[-1]
        if len(ano_str) == 4 and ano_str.isdigit():
            ano_nasc = int(ano_str)
            idade = ano_hoje - ano_nasc

         # Mostra informações
            print(f"\nPessoa {pessoas}:")
            print(f"Data: {'/'.join(data_com_barra)}")
            print(f"Ano: {ano_nasc}")
            print(f"Idade: {idade} anos")
            if  idade < 18:
                menor_idade += 1
            elif idade >= 18:
                maior_idade += 1
        else:
            print("Ano inválido! Deve ter 4 dígitos.")
    else:
        print('Formato inválido! Use DD/MM/AAAA')

print('-' * 80)

print(f"\n{'='*80}")
print(f"O total de pessoas maior de idade {maior_idade}")
print(f"O total de pessoas menores de idade {menor_idade}")
