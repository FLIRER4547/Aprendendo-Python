
n1=int(input('digite um valor em metros:'))
a=input('agora diga se quer que esse valor seja conveertido para centimetros ou milimetros (digite (C) OU (M))').lower().strip()
if a=='c':
          c=n1*100
          print(f'{n1} metros convertido para centimetros é: {c}cm')
elif a=='m':
            m=n1*1000
            print(f'{n1} metros covertido para milimetros é:{m}mm')
else:
     print('não compreendi sua resposta, tente novamente')

