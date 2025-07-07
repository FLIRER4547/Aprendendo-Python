
a=input('posso calcular sua média escolar, você gostaria desde serviço?(SIM OU NÃO)').lower().strip()
if a=='sim':
            print('ótimo vou precisar das suas notas...')
            n1=float(input('qual foi a sua primeira nota?'))
            n2=float(input('qual foi a sua segunda nota?'))
            m=(n1+n2)/2
            print(f'sua média foi de {m:.2f}')
            if m<=6.0:
                      print('cuidado em meu man, tá baixa demais essa notinha aí')
            elif m>=8.9:
                        print('calma aê Albert Einstein kkkk')
elif a=='não' or  a=='nao':
                       print('tá com vergonha cara? eu não julgo notas...não ainda kkk')
else:
     print('não entendi sua resposta meu caro, tente novamente...')
