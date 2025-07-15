##'°1 METODO#####
n=input('Digite três números separados por espaços: ').strip()
n1=n.split()[0]
n2=n.split()[1]
n3=n.split()[2]
print(f'O maior número é: \033[1;35m{max(int(n1),int(n2),int(n3))}\033[0m')

