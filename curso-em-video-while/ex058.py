from time import sleep
from random import randint

contador = 1
maquina = randint(0,10)
user = int(input("Qual número de  0 à 10 eu pensei: "))
while maquina != user:
        print("Processando ...")
        sleep(1)
        print('Você errou!')
        contador += 1
        user = int(input("Tente novamente: "))
        

print("Processando ...")
sleep(1)
print('Nossa você acertou')

print(f'Você fez um total de {contador} tentativas!')



