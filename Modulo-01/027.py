from datetime import datetime
hr=datetime.now().strftime('%H')
a=str(input('Escreva seu nome completo: ')).strip().lower()
if int(hr)>5 and int(hr)<12:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha um bom dia')
elif int(hr)>11 and int(hr)<19:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha uma boa tarde')
else:
    print(f' olá \033[1;4;31m{a.split()[0].capitalize()}\033[0m \033[1;4;31m{a.split()[-1].capitalize()}\033[0m, tenha uma boa noite')






                                         #METODO GUANABARA###
#n=str(input('Digite seu nome: ')).lower().strip()
#print(f'seu primeiro nome é {n[0]}')
#print(f'Seu ultimo nome é {n[len(n)-1]}')
