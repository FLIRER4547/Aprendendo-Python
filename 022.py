


import random

al=int(random.randint(0,5))
n=int(input('tente adivinhar o número de 1 a 5 que vou escolher...'))
if n==al:
         print(f'você acertou! eu realmente estava pensando no número {al}, meus parabéns!!')
elif n > 5 or n < 0:
    print('como que tu errou cara? era p digitar um número entre 0 e 5, tu é burro? poha...')
else:
     print(f'que peninha, eu estava pensando em {al},')

