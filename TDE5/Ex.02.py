# 2. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.
for tabuada in range(1, 11):
    print(f'\nTabuada do {tabuada}\n')
    for n in range(1, 11):
        print(f'{tabuada} x {n} = {tabuada * n}')