def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1

    elif valor < 2000:
        imposto = valor * 0.13

    else:
        imposto = valor * 0.2

    return imposto

preço_produto1 = 2500
preço_produto2 = 3500
imposto_produto1 = calcular_imposto(preço_produto1)
imposto_produto2 = calcular_imposto(preço_produto2)

print(imposto_produto1)
print(imposto_produto2)
