from random import shuffle


print('coloque os nomes de quatro alunos abaixo e uma ordem aleaiória será selecionada')
a=input('primeiro aluno:')
b=input('segundo aluno:')
c=input('terceiro aluno:')
d=input('e por fim, o quarto aluno:')
lst=[a,b,c,d]
shuffle(lst)
print(f' a ordem sortiada foi: {lst}')




