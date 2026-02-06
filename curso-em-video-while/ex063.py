quantidade = int(input("Escreva a quantidade de termos: "))
termo_1 = 0
termo_2 = 1
print(f"Sequancia começa com: {termo_1} e {termo_2}")
print("-=-" * 30)

print(f"a1 = {termo_1}")
print(f"a2 = {termo_2}")
termo_anterio = termo_1
termo_atual = termo_2
contador = 3
while contador <= quantidade:
    proximo_termo = termo_anterio + termo_atual
    print(f"a{contador} = {proximo_termo}")

    termo_anterio = termo_atual
    termo_atual = proximo_termo
    contador += 1


