num = int(input('Digite um número: '))
print('A tabuada deste número é: ')
for c in range(1, 10+1):
    print(' {} x {} = {}'.format(num, c, num*c))
