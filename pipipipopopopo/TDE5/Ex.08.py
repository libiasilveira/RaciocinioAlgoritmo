''' 9. Elabore um programa que leia um vetor de 10 posições inteiras. 
Depois, solicite para o usuário um número que ele gostaria de 
pesquisar neste vetor, caso o número exista no vetor, mostre em
qual(is) posição(ões) ele foi encontrado e quantas ocorrências 
foram detectadas.'''

numeros = []
for i in range(1, 11):
    n = int(input(f'Coloque o {i}° número inteiro do vetor: '))
    numeros.append(n)

pesquisado = int(input('Entre com o número a ser pesquisado: '))

ocorrencias = 0
posicoes = []

for i in range(len(numeros)):
    if numeros[i] == pesquisado:
        ocorrencias += 1
        posicoes.append(i)

if ocorrencias > 0:
    print(f'O número {pesquisado} foi encontrado {ocorrencias} vez(es) nas posições: {posicoes}')
else:
    print(f'O número {pesquisado} não foi encontrado no vetor.')
