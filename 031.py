km=int(input('a viagem é de quantos km? '))
if km<200:
    print(f'O valor da sua passagem é de \033[1;32mR${km*0.50:.2f}\033[0m.')
if 200< km <1000:
    print(f'O valor da sua passagem é de \033[1;32m{km*0.45:.2f}\033[0m.')
else:
    print('Acho melhor ir de avião kkkkk')