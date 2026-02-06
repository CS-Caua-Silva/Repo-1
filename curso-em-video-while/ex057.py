from time import sleep

sexo = "M" or "F"
sexo = m = f = 0
cont = "s"
while cont == "s":
    sexo = str(input("Digite seu sexo [M/F]: ")).upper()
    cont = str(input("Quer continuar? [S/N]:  ")).lower()
    if sexo == "M":
        m += 1
    if sexo == "F":
        f += 1
print("-" * 20)
print("Processando dados...")
sleep(2)
print("-" * 20)
print(f"O total de pessoas do sexo masculino é {m} e o total de sexo femenino: {f}")


