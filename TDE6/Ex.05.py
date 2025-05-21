from random import sample

m = []
for line in range(15):
    line = sample(range(10, 100), 7)
    m.append(line)


print("Matriz:")
for line in m:
    print(line)

pares = []
impares = []
for line in m:
    for num in line:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

new_line = pares + impares

index = 0
for line in range(15):
    for column in range(7):
        m[line][column] = new_line[index]
        index += 1

print("\nMatriz Modificada:")
for line in m:
    print(line)
