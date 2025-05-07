# 10. Desenvolva um programa que leia 10 números inteiros e armazene-os 
# em um vetor chamado vLido. Depois, crie dois outros vetores: vPares, 
# contendo somente os números pares de vLido, e vImpares contendo 
# somente os números ímpares de vLido. Os vetores vPares e vLido 
# não deverão conter zeros. Mostre então os três vetores.

vLido = []
vPares = []
vImpares = []
for i in range(1,11):
    num = int(input(f'Coloque o {i}° número para ser adicionado na lista: '))
    if num != 0:
        vLido.append(num)

        if num % 2 == 0:
            vPares.append(num) 
        else:
            vImpares.append(num)

print(f'A lista de valores lidos é: {vLido}.')
print(f'A lista de valores lidos pares é: {vPares}.')
print(f'A lista de valores lidos ímpares é: {vImpares}.')