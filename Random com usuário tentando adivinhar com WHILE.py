from random import randint


print("""Será que você consegue adivinhar em qual número o computador pensou?\n
Tente um número de 0 a 10\n\n""")
numero = int(input('Digite um número: '))
print('Sorteando...')
random = randint(0, 10)
while numero != random:
    numero = int(input('Você errou, tente outro número: '))
    print('Sorteando...')
else:
    print('Você acertou! Eu pensei no número {}!'.format(random))
