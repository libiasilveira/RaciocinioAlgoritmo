# A partir do código abaixo, escreva 

b = True
while b:
    a = int(input(': '))
    x = a // 2
    s = 0
    s1 = 0
    x += a % 2
    for i in range(0,x):
        s1 += a - (x + i) # soma a variável o resultado do após 
        s += a - i
    print('s:', s, 's1:', s1)
    b = input(': ') == 's' # teste lógico: se o usuário colocar s, será True, logo o loop continuará. se for False, interrompe


    # diga a funcionalidade e depois dada uma entrada, execute. faça teste de mesa