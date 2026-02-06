
a1 = float(input("Digite o Primeiro termo: ")) # qual numero vai iniciar
r = float(input("Razão: ")) # quantas casas ele vai pular
n = float(input("Quantos termos? ")) # quantidade que vai aparecer na tela

contador = 1 # Começa no primeiro termo
termo = a1 # Termo que estamos calculando

while contador <= n:
    print(f"{contador} = {termo}")
    termo = termo + r
    contador += 1