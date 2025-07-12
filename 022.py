<<<<<<< HEAD

import random

al=int(random.randint(0,5))
n=int(input('tente adivinhar o número de 1 a 5 que vou escolher...'))
if n==al:
         print(f'você acertou! eu realmente estava pensando no número {al}, meus parabéns!!')
elif n > 5 or n < 0:
    print('como que tu errou cara? era p digitar um número entre 0 e 5, tu é burro? poha...')
else:
     print(f'que peninha, eu estava pensando em {al},')
=======
a=input('digite seu nome completo: ')
print(f'A sua frase em lower é: \033[1;4;35m{a.lower().strip()}\033[0m')
print(f'A frase em upper é: \033[1;4;35m{a.upper().strip()}\033[0m')
print(f'A frase tem um total de \033[1;4;35m{len(a.strip())}\033[0m letras.')
print(f'A primeira palavra da frase tem um total de \033[1;4;35m{len(a.split()[0])}\033[0m letras')
>>>>>>> 0af5b84 (adicionar todos os arquivos)
