t = input('''Digite o valor das retas a,b,c e será analisado se elas podem formar um triângulo,
 \033[1mna digitação separe os valores por espaços:\033[0m ''').strip()
a, b, c = map(float, t.split())
if a + b > c and a + c > b and b + c > a:
    print('Os valores podem sim formar um triângulo')
else:
    print('\033[1mos valores \033[4;31mNÃO\033[0m \033[1mpodem formar um triangulo\033[0m')