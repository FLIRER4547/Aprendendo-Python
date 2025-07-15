y=int(input('em que ano você está? ').strip())
y1=y%4
if y1>0:
    print('\033[1;31mNão é um ano bissexto\033[0m')
else:
    print('\033[1;32mSeu ano é um ano bissexto\033[0m.')