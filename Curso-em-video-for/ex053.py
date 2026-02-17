#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:


texto = str(input("Digite uma palavra ")).strip().lower()
texto_sem_espaços = ''.join(filter(str.isalnum, texto))

# Verificar
he_palindromo = True
tamanho = len(texto_sem_espaços)

# loop
for palavra in range(tamanho // 2):
    if texto_sem_espaços[palavra] != texto_sem_espaços[tamanho- 1 - palavra]:
        he_palindromo = False
        break

if he_palindromo:
    print("É um palíndromo ✅")
else:
    print("Não é um palíndromo ❌")

print(f"Texto normal: {texto}")
print(f"Texto invertido: {texto[::-1]}")
