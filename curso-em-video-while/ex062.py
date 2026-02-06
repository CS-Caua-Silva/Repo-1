






a1 = float(input("Digite o Primeiro termo: ")) # qual numero vai iniciar
r = float(input("Razão: ")) # quantas casas ele vai pular
n = float(input("Quantos termos? ")) # quantidade que vai aparecer na tela

contador = 1 # Começa no primeiro termo
termo = a1 # Termo que estamos calculando

while contador <= n:
    
    print(f"{contador} = {termo}")
    termo = termo + r
    contador += 1

extra =  int(input("Quantos termos a mais? (0 para sair): "))
    
while extra > 0:  
    print(f"\n➕ {extra} TERMOS ADICIONAIS:")
    print("\n" + "="*30)

    contador_extra = 0
    while contador_extra < extra:
        print(f'{contador} =  {termo}')
        termo += r
        contador += 1
        contador_extra += 1
    print("\n" + "="*30)
    extra =  int(input("Quantos termos a mais? (0 para sair): "))

print(f"\n✅ Fim! Total: {contador-1} termos")


