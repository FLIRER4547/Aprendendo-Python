s=int(input('Digite seu salário: '))
if s>1250:
    print(f'Parabéns! seu salário teve um aumento de \033[1;4;35m10%\033[0m e agora é: \033[1;4;32mR$:{(((s*10)/100)+s):.2f}\033[0m.')
if s==1250 or s<1250:
    print(f'Parabéns! seu salário recebeu um aumento de \033[1;4;35m15%\033[0m e agora é: \033[1;4;32m{(((s*15)/100)+s):.2f}\033[0m.')