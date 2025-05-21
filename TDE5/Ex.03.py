# 3. Leia três números do teclado e 
# verificar se o primeiro é maior que a soma dos outros dois.

nums = []
for i in range(1,4):
    num = float(input(f'Digite o {i}° número: '))
    nums.append(num)

soma = nums[1] + nums[2]

if nums[0] > soma:
    print('O primeiro número é maior que a soma dos outros dois. A soma deu:', soma, '.')
else:
    print('O primeiro não é maior que a soma dos outros dois. A soma deu:', soma, '.')
