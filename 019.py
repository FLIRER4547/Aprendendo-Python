
import random

print('coloque o nome de quatro alunos abaixo, um deles será sorteado para limpar a lousa')
a=input('primeiro aluno:')
b=input('segundo aluno:')
c=input('terceiro aluno:')
d=input('E por fim, o quarto:')
lt=[a,b,c,d]
print(f'o escolhido para limpar a lousa é: {random.choice(lt)}')

