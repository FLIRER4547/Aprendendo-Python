
'''from math import sqrt

a=input('vamos calcular a hipotenusa de um triângulo juntos?(digite sim ou não):').lower().strip()
if a=='sim':
            cp=float(input('qual o valor do cateto oposto?'))
            ca=float(input('qual o valor do cateto adjascente?'))
            print(f'a hipotenusa desse triângulo é igual a: {sqrt(cp**2+ca**2):.2f}')
elif a=='não' or a=='nao':
                          print('ok, se mudar de ideia estarei aqui!')'''


from math import hypot
cato=float(input('qual o valor do cateto oposto?'))
cata=float(input('qual o valor do cateto adjascente?'))
print(f'a hipotenusa desse triângulo é igual a: {hypot(cato,cata):.2f}')

