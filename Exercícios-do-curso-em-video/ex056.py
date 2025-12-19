#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem_mais_velho = 0
nomes_homem_mais_velho = []
mulheres_menos_20 = 0
soma_idades = 0

for pessoa in range(4):
    nome = input(f"Digite o nome da pessoa {pessoa + 1}: ")
    idade = int(input(f"Digite a idade da pessoa {pessoa + 1}: "))
    sexo = input(f"Sexo (M/F) da pessoa {pessoa + 1}: ").strip().lower()

    soma_idades += idade

    if sexo == "f" and idade < 20:
        mulheres_menos_20 += 1

    if sexo == "m":
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nomes_homem_mais_velho = [nome]
        elif idade == homem_mais_velho:
            nomes_homem_mais_velho.append(nome)

media = soma_idades / 4

print("-" * 60)
print(f"Média de idade do grupo: {media:.1f} anos")
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")

if nomes_homem_mais_velho:
    if len(nomes_homem_mais_velho) == 1:
        print(f"O homem mais velho é {nomes_homem_mais_velho[0]} com {homem_mais_velho} anos.")
    else:
        print(f"Homens mais velhos (empate com {homem_mais_velho} anos):")
        for nome in nomes_homem_mais_velho:
            print(f"- {nome}")
else:
    print("Não há homens no grupo.")
