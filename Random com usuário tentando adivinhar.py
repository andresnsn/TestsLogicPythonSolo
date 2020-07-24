from random import randint
from time import sleep
print("""Será que você consegue adivinhar em qual número o computador pensou?\n
Tente um número de 0 a 10\n\n""")
numero = int(input('Digite um número: '))
print('Sorteando número...')
sleep(3)
random = randint(0, 10)

if numero == random:
    print('Parabéns, você acertou o número! ')
else:
    print('Você errou o número! Eu pensei no número {} '.format(random))
