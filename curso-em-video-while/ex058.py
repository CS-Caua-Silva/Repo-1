from time import sleep
from random import randint

contador = 1
maquina = randint(0,10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10")
print("Será que você consegue adivinhar qual foi?")
user = int(input("Qual número de  0 à 10 eu pensei: "))

while maquina != user:
        print('Você errou!')
        contador += 1
        user = int(input("Tente novamente: "))
        if user < maquina:
                print("Haha... Tente mais")
        if user > maquina:
                print("Haha... Tente menos")

print("---" * 20)
print("Processando ...")
sleep(1)
print('Nossa! você acertou!')
print(f'Você fez um total de {contador} tentativas!')
