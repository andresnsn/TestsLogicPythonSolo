maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual peso da {} pessoa?'.format(c)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))

# Interessante estudar isto posteriormente, para entender a lógica de programação por trás da identificação de maiores e menores valores.