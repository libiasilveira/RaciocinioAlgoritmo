# 8. Elabore um programa que leia um vetor de 10 posições inteiras e 
# então mostre o valor máximo,
#  o valor mínimo e a amplitude amostral do conjunto fornecido.

numeros = []
for i in range(1,11):
    num = int(input(f'Coloque o {i}° número do vetor: '))
    numeros.append(num)

amplitude = max(numeros) - min(numeros)

print(f'O valor máximo desse vetor é {max(numeros)} e o valor mínimo é {min(numeros)}.')
print(f'A amplitude amostral desse vetor é {amplitude}.')