# 6. Ler 4 números inteiros e calcular a soma dos que forem par. 

pares = 0
for n in range(1,5):
    numero = int(input(f'Insira o {n}° número: '))
    if numero % 2 == 0:
        pares += numero

print('A soma dos valores pares é:', pares)