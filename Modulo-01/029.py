km=float(input('A quantos quilometros por hora você está? ').strip())
if 80< km <120:
    print(f'Sua velociadade está \033[1;31macima\033[0m da permitida, você recebeu uma multa de R$:\033[1;4;31m{(km-80)*7:.2f}\033[0m.')
if km>120 or km==120:
    print('Sua velocidade está \033[1;31mMUITO ACIMA\033[0m do \033[1;4;35mPERMITIDO\033[0m.')
    print(f'\033[1;33mVocê foi\033[0m \033[1;31mMULTADO em R$:{(km-80)*7:.2f}.')
else:
    print('Sua velocidade está \033[1;32mdentro\033[0m limites permitidos.')