'''11. Escreva um programa que leia um vetor de números inteiros 
de 10 posições, aceitando apenas valores positivos. 
Modifique então o vetor de forma que, tenhamos primeiro 
todos os números pares, depois, os números impares. 
Mostre o vetor antes de depois da modificação.'''

print('Olá! Somente os números positivos serão armazenados.')
positivos = []
pares = []
impares = []
for i in range(1,11):
    num = int(input(f'Coloque o {i}° número positivo do vetor: '))
    if num >= 0:
        positivos.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

print(f'A lista de números positivos inseridos: {positivos}.')
print(f'A lista modificada, que tem primeiro todos os números pares, depois, os números impares: {pares + impares}.')