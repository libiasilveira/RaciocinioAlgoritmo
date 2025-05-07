# 7.Dizemos que um número natural é triangular se ele é 
# produto de três números naturais consecutivos. 
# Dado um inteiro não-negativo n, verificar se n é triangular.

n = int(input('Coloque um número inteiro positivo: '))

x = 1
triangular = False

while x * (x + 1) * (x + 2) <= n:
    if x * (x + 1) * (x + 2) == n:
        triangular = True
        break
    x += 1

if triangular:
    print(f'{n} é um número triangular (produto de {x}, {x + 1} e {x + 2})')
else:
    print(f'{n} não é um número triangular.')
