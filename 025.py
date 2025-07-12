a=input('Digite seu nome completo: ').lower()
b='silva' in a
if b==True:
    print(f'Meus parabens \033[1;32m{a.split()[0].capitalize()}\033[0m, você faz parte da familia \033[1;4;35mSilva\033[0m!!')
if b==False:
    print(f'è uma pena você não fazer parte da familia \033[1;4;35mSilva\033[0m, mas seu nome ainda é muito legal')
