t=input('''Digite o valor das retas a,b,c e será analisado se elas podem formar um triângulo, na digitação separe 
os valores por espaços: ''').strip()
a,b,c= map(int,t.split())
if a+b>c and a+c>b and b+c>a:
    print('Os valores podem sim formar um triângulo')
else:
    print('os valores não podem formar um triangulo')