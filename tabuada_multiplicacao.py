# Desenvolvedor Brevetecno
# Python 3.7
# 2019

while True:
    # Insere o número que deve ser multiplicado de 0 até 10
    n = int(input('Número: '))

    print('='*18)

    # Multiplica o número inserido por 0 até 10
    for vez in range(11):
        # Mostra o resultado
        print('{} x {} = {}'.format(n, vez, n * vez))
        
    print('='*18)
    fim = input('Aperte uma tecla para continuar...')
