from time import sleep

print('PRESSIONA QUALQUER TECLA PARA CONTINUAR')
input()
print('Carregando...')
sleep(2)
valor = int(input('Digite o valor de seu saque: '))
nota = valor//100
print('Serão {} notas de 100'.format(nota))
valor = valor % 100
nota = valor // 50
print('{} notas de 50'.format(nota))
valor = valor % 50
nota = valor // 20
print('{} notas de 20'.format(nota))
valor = valor % 20
nota = valor // 10
print('{} notas de 10'.format(nota))
valor = valor % 10
nota = valor // 1
print('{} moedas de 1'.format(nota))
