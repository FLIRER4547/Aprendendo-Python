n1=float(input('quantos reais tem na sua carteira?'))
x=input('você quer converter seu dinheiro para Dolár ou Euro?(digite (E) ou (D):').lower().strip()
if x=='e':
          e=n1/6.44
          print(f'você tem {e:.2f} euros em sua carteira')
elif x=='d':
            d=n1/5.46
            print(f'você tem {d:.2f} doláres em sua carteira')
else:
     print('não entendi sua resposta, tente novamente...')


