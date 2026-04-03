'''
quantidade = int(input("Escreva a quantidade de termos: "))
termo_1 = 0
termo_2 = 1
print('~' *30)
print(f"Sequancia começa com: {termo_1} e {termo_2}")
print('~' * 30)

print(f"a1 = {termo_1}")
print(f"a2 = {termo_2}")

# Formular para a sequência funcionar
termo_anterio = termo_1
termo_atual = termo_2
contador = 3 # Como ja temos o T1 e T2, vamos começar no 3

while contador <= quantidade:
    proximo_termo = termo_anterio + termo_atual
    print(f"a{contador} = {proximo_termo}")

    termo_anterio = termo_atual
    termo_atual = proximo_termo
    contador += 1

'''
# A cima temos uma forma de fazer esse exercício e baixo outra.


quantidade = int(input("Digite a quantidade de termos: "))

t1 = 0
t2 =  1
cont = 3

print("~" *30)
print(f"{t1} -> {t2}",  end=' ')

while cont <= quantidade:
    t3 = t1 + t2
    print(f" -> {t3}", end=' ')
    t1 = t2 
    t2 = t3
    cont += 1

print(" -> Fim")
print("~" *30)
