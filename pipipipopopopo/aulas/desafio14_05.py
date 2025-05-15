'''implementar um código Python que cria uma matriz com as dimensões 
que o usuário especificar preenchendo com valor 1'''

m = []
linhas = int(input('Entre com a quantidade de linhas: '))
colunas = int(input('Entre com a quantidade de colunas: '))

# para construir uma matriz, temos que construir linha por linha e depois, construir a matriz
for linha in range(linhas):
    linha_matriz = []
    for coluna in range(colunas):
        linha_matriz.append(1)
    m.append(linha_matriz)

for linha in range(linhas):
    for coluna in range(colunas):
        print(m[linha][coluna], end=' ')
    print('')