from random import randint
while True:
    n=int(input('Digite um número de 0 a 5: ').strip())
    if 0 <= n < 6:
        s=randint(0,5)
        if n==s:
            print('\033[1;4;35mMeus parabéns!!!\033[0m você acertou o número que eu estava pensando!')
        else:
            print('não era nesse número que eu estava pensando, \033[1;4;31mtente de novo!\033[0m')
    else:
        print('O número escolhido só pode estar entre 0 e 5, tente de novo.')
        n=int(input('\033[1;31mDigite um número de 0 a 5\033[0m: ').strip())

