primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = (razao * 10 + primeiro) - razao

while primeiro <= decimo:
    print(primeiro, end = ' ')
    primeiro += razao