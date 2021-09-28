produto = []
carrinho = []

print('{:>15}'.format('BEM-VINDO!'))

while True:
    print('''
[1] Escolher produto
[2] Ver carrinho de compras
[3] Editar carrinho
[4] Excluir produto
[5] Sair
''')
    
    opc = int(input('\nEscolha uma das opções: '))
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    if opc == 1:
        produto = str((input('\nQual produto você deseja colocar no carrinho? ')))
        carrinho.append(produto[:])
        
        #print(carrinho)
        #print(produto)
        
    elif opc == 2:
        print('\nSeu carrinho:\n')
        
        for p in carrinho:    
            print(p)
            
    elif opc == 3:
        edit_pos = int(input('\nDigite a posição do item que você quer trocar: '))
        edit_prod = str(input('Digite o nome do novo produto: '))
        carrinho[edit_pos] = edit_prod
        
        #print(carrinho)
        
    elif opc == 4:
        exc = int(input('\nDigite a posição do item que será removido: '))
        carrinho.pop(exc)
        
        #print(carrinho)
    
    elif opc == 5:
        print('\nSaindo...')
        break
