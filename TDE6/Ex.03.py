'''3. Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros,
sorteados dentro do intervalo 100 a 999, garantindo que não haverá nenhuma repetição
(os 16 números devem ser únicos). Encontre então o valor do menor elemento da linha
em que se encontra o maior elemento da matriz. Mostre a matriz e os dois valores
encontrados'''

from random import sample

m = []
for i in range(1,5):
    linha = sample(range(100, 1000), 4)
    m.append(linha)

biggest = m[0][0]
line_big = None

for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] > biggest:
            biggest = m[i][k]
            line_big = i

small = min(m[line_big])

print("Matriz:")
for line in m:
    print(line)

print("\nMaior elemento da matriz:", biggest)
print("Linha onde está o maior elemento:", line_big)
print("Menor elemento dessa linha:", small)

