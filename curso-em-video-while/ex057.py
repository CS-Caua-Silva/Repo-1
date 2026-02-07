from time import sleep
sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("-" * 20)
print("Processando dados...")
sleep(2)
print(f"Sexo {sexo} registrado com sucesso")



