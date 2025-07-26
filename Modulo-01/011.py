
a=input('quer que eu calcule a área da sua parede e quanto litros de tinta ela precisa?(digite SIM OU NÃO)').lower().strip()
if a=='sim':
            b=float(input('qual o comprimento da sua parede?'))
            h=float(input('qual a altura da sua parede?'))

            r=(b*h)
            t=r / 2
            print(f'sua parede tem uma área de {r:.2f} metros quadrados')
            print(f'essa parede precisa de {t:.1f} litros de tinta para ser completamente pintada')
elif a=='não' or a=='nao':
                          print('ok, tudo bem, mas estarei aqui caso mude de ideia!')
else:
     print('não entendi a sua resposta, tente novamente')