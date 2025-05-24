'''Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação. '''

from random import sample

m = []
for line in range(15):
    line = sample(range(10, 100), 7)
    m.append(line)


print("Matriz:")
for line in m:
    print(line)

impares = []
pares = []
for line in m:
    for column in m:
        if m[line][column] % 2 == 0:
            pares.append(m[line][column])
        else:
            impares.append(m[line][column])

m2 = pares + impares

print("\nMatriz Modificada:")
for line in m:
    print(line)
