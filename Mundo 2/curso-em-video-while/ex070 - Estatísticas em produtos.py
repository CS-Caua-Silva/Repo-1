print('-' * 20)
print('  lOJA ')
print('-' * 20)

soma = 0
produto_mais_1000 = 0
menor_preço = None
nome_produto_menor = ''

while True:
    produto = str(input('Nome do Produto: '))
    if produto == '':
     continue

    # Preço 
    while True:
        preço_str = (input('R$ '))
        
        if preço_str == '':
           continue

        if preço_str.isdigit():
           preço = float(preço_str)
           soma += preço
           break
        

    if preço > 1000:
       produto_mais_1000 += 1

    if menor_preço is None or preço < menor_preço:
        menor_preço = preço
        nome_produto_menor = produto
    
    #continue
    while True:
       cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
       if cont == 'S':
          break
       else:
          break
    if cont == 'N':
       break


print(f'O total de produtos que tiveram um preçoa cima de 1 mil foi de {produto_mais_1000}')
print(f'A soma dos produtos é de {soma}')
print(f'O produto de menor valor foi {nome_produto_menor} que custou {menor_preço}')

     