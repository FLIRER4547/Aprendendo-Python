km=int(input('A quantos quilometros por hora você está? ').strip())
if km>80:
    print(f'Sua velociadade está \033[1;31macima\033[0m da permitida, você recebeu uma multa de R$:\033[1;4;31m{(km-80)*7:.2f}\033[0m.')
else:
    print('Sua velocidade está \033[1;32mdentro\033[0m limites permitidos.')