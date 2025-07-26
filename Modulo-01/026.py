a=str(input('escreva uma frase: ')).lower().strip()
l=input('qual letra que encontrar na frase? ')
print(f' a letra \033[1;4;31m{l.upper()}\033[0m aparece \033[1;4;31m{a.count(l)}\033[0m vezes na frase.')
p=a.find(l)
s=a.rfind(l)
if p==-1:
    print('\033[1;31mA letra não foi encontrada na frase.\033[0m')
else:
    print(f'Aparece primeiro na posição \033[1;4;31m{p+1}\033[0m')
    print(f'E por ultimo na posição \033[1;4;31m{s+1}\033[0m')

