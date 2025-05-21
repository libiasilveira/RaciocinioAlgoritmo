'''12. Construa um programa que sugira uma aposta de Mega-Sena ou seja, 
um algoritmo que gera e mostra um conjunto de 6 números aleatórios 
entre [1, 60] sem repetição. Em seguida, obtenha a aposta do usuário 
(sem repetição) e indique quantos acertos ele teve. '''

import random

mega_sena = random.sample(range(1, 61), 6)

aposta = []
for i in range(1,7):
    num = int(input(f'Coloque o {i}° número de 1 a 60 da sua aposta na Mega-Sena: '))
    if num not in aposta :
        aposta.append(num)
    else:
        print('Não aceitamos números repetidos para a aposta.')

acertos = 0
for n in range(len(mega_sena)):
    if aposta[n] in mega_sena:
        acertos += 1

print(f'A Mega-Sena sorteou esse conjunto de números:{mega_sena}')
print(f'A sua aposta foi essa:{aposta}')

if acertos > 0:
    print(f'Você teve {acertos} acerto(s)! Parabéns!')
else:
    print('Você não teve nenhum acerto. Que pena!')