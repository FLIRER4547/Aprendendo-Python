a=input('digite o nome de uma cidade: ').lower().rstrip().lstrip()
b=('santo' in (a.split()[0]))
if b==True:
    print('''a cidade começa com 'Santo' ''')
if b==False:
    print('''O nome da cidade não começa com 'Santo' ''')



#METODO GUSTAVO GUANABARA##
#c=input('Digite o nome da sua cidade: ').strip().lower()
#print(c[:5] == 'santo')