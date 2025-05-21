'''Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e 
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo 
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e 
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.'''


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 1, 2, 3],
     [4, 5, 6, 7]]

print("Matriz (4 x 4):")
for linha in m:
    print(linha)

array = []

for coluna in range(4):
    bigest = m[0][coluna]
    for linha in range(4):
        if m[linha][coluna] > bigest:
            bigest = m[linha][coluna]
    array.append(bigest)


print("\nArray com os maiores valores de cada coluna:")
print(array)

media = sum(array) / len(array)
print(f"\nMédia aritmética dos maiores valores: {media:.2f}")