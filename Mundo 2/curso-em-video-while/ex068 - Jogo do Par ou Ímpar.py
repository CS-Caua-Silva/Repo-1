from random import randint

contador = 0

print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 10)

while True:
    maquina = randint(0,10)
    user = int(input('Digite um valor: '))
    escolha = ' '
    soma = user + maquina
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Você: {user}| PC: {maquina}| o total foi: {soma}')
    print('=-' * 10)
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu! 🏆')
            contador += 1
            print(f'🔥 Sequência: {contador}')
        else:
             print('Você Perdeu!')
             break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você venceu! 🏆')
            contador += 1
            print(f'🔥 Sequência: {contador}')
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar de novo ...')
    
            
print(f'GAME OVER! O seu total de vitórias ficou em: {contador} 🏆')
print('🎮 Fim de jogo. Volte sempre!')
