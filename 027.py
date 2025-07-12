from datetime import datetime
hr=datetime.now().strftime('%H')
a=input('Escreva seu nome completo: ')
if int(hr)>5 and int(hr)<12:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha um bom dia')
elif int(hr)>11 and int(hr)<19:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha uma boa tarde')
else:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha uma boa noite')
