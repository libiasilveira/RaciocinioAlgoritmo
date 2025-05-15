'''Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij'''

m = []
multiplicador = int(input('Coloque o número que multiplicará a sua matriz: '))
for linha in range(3):
    linha_matriz = []
    for coluna in range(3):
        num = int(input('Coloque um número para adicionar na matriz:'))
        linha_matriz.append(multiplicador * num)
    m.append(linha_matriz)
print(f'Essa é a nova matriz formada: {m}')
