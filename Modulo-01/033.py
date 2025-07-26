##'°1 METODO#####
n=input('Digite três números separados por espaços: ').strip()
n1=n.split()[0]
n2=n.split()[1]
n3=n.split()[2]
print(f'O maior número é: \033[1;35m{max(int(n1),int(n2),int(n3))}\033[0m')



##METODO GUANABARA#########
'''a=int(input('Primeiro valor: '))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor: '))
menor=a
if b<a and b<c:
    menor=b
if c<b and c<a:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>b and c>a:
    maior=c
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')'''
