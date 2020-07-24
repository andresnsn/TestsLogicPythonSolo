lista = ['', '', '', '', '']
contador = 0
for c in range(1, 6):
    peso = str(input('Qual o peso da {} pessoa? '.format(c)))
    lista[contador] = peso
    contador += 1
lista.sort()
print('O menor peso inserido foi {}, e o maior peso inserido foi {}!'.format(lista[0], lista[4]))
