
a=input('você gostaria de traformar Ceusius para Fahrenheint ou para Kelvin?(digite: (F) ou (k)').lower().strip()
if a == 'f':
         c=float(input('qual a temperatura a ser convertida? °C:'))
         f=c*(9/5)+32
         print(f'a temperatura {c}°C convertido para Fahrenheit é igua a {f}°F.')
elif a == 'k':
              c=float(input('qual a temperatura que deseja converter °C:'))
              print(f'a temperatura de {c}°C convertido para Kelvin é igual a {c+273.15}°K.')
else:
     print('desculpe, não compreendi sua resposta, tente novamente')

