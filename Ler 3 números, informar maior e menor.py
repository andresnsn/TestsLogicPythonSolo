num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

lista = [num1, num2, num3]
lista = sorted(lista)
print('O maior número é {} e o menor número é {}'.format(lista[2], lista[0]))
