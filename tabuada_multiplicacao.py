# Desenvolvedor Brevetecno
# Python 3.7
# 2019

while True:
    print('='*18)
    
    print('(0) - Sair')
    print('(1) - Soma')
    print('(2) - Subtração')
    print('(3) - Multiplicação')
    print('(4) - Divisão')
    
    print('='*18)
    
    valor = int(input('Resposta: '))
    
    print('='*18)
    
    # Encerra
    if (valor == 0):
        print('Saindo...')
        exit()
        
    # Soma
    elif (valor == 1):
        print('='*18)
        valor = int(input('Tabuada de soma do número: '))
        min = int(input('De: '))
        max = int(input('Até: '))
        
        for n in range(max):
            print('{} + {} = {}'.format(valor, n, (valor + n)))

    # Subtrair
    elif (valor == 2):
        print('='*18)
        valor = int(input('Tabuada de subtração do número: '))
        min = int(input('De: '))
        max = int(input('Até: '))
        
        for n in range(max):
            print('{} + {} = {}'.format(valor, n, (valor - n)))

    # Multiplicar
    elif (valor == 3):
        print('='*18)
        valor = int(input('Tabuada de multiplicação do número: '))
        min = int(input('De: '))
        max = int(input('Até: '))
        
        for n in range(max):
            print('{} + {} = {}'.format(valor, n, (valor * n)))

    # Dividir
    elif (valor == 4):
        print('='*18)
        valor = int(input('Tabuada de divisão do número: '))
        min = int(input('De: '))
        max = int(input('Até: '))
        
        for n in range(max):
            print('{} + {} = {}'.format(valor, n, (valor / n)))

