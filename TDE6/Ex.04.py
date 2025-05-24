'''Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores'''
from random import sample

m = []
for line in range(5):
    line = sample(range(10, 100), 5)
    m.append(line)


print('\nA matriz gerada')
for line in range(len(m)):
    for column in range(len(m[line])):
        print(m[line][column], end=' | ')
    print("")

sum_a = 0
print('\nMatriz A')
for line in range(len(m)):
    for column in range(len(m[line])):
        if column == 2 or line == 2:
            print(m[line][column], end=' | ')
            sum_a += m[line][column]
        else:
            print(0, end= ' | ')
    print("")
print(f'\nSoma dos elementos da matriz A: {sum_a}')

sum_b = 0
print('\nMatriz B')
for line in range(len(m)):
    for column in range(len(m[line])):
        if line == 0 or line == 4 or column == 0 or column == 4:
            print(m[line][column], end=' | ')
            sum_b += m[line][column]
        else:
            print(0, end= ' | ')
    print("")
print(f'\nSoma dos elementos da matriz B: {sum_b}')

sum_c = 0
print('\nMatriz C')
for line in range(len(m)):
    for column in range(len(m[line])):
        if line - column == 1 or column - line == 1:
            print(m[line][column], end=' | ')
            sum_c += m[line][column]
        else:
            print(0, end= ' | ')
    print("")
print(f'\nSoma dos elementos da matriz C: {sum_c}')

sum_d = 0
print('\nMatriz D')
for line in range(len(m)):
    for column in range(len(m[line])):
        if line == (column - 1) or line == (column + 1) or column == (line - 3) or column == (line + 3):
            print(m[line][column], end=' | ')
            sum_d += m[line][column]
        else:
            print(0, end= ' | ')
    print("")
print(f'\nSoma dos elementos da matriz D: {sum_d}')