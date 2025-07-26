s=float(input('Digite seu salário: '))
if s==1250 or s<1250:
    s1=s*0.15+s
    print(f'Parabéns! seu salário recebeu um aumento de \033[1;4;35m15%\033[0m e agora é: \033[1;4;32m{s1:.2f}\033[0m.')
else:
    s1=s*0.10+s
    print(f'Parabéns! seu salário teve um aumento de \033[1;4;35m10%\033[0m e agora é: \033[1;4;32mR$:{s1:.2f}\033[0m.')