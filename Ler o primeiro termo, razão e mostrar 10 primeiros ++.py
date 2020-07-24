primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = (razao * 10 + primeiro) - razao
numero = 1
while primeiro <= decimo:
        print(primeiro, end=' ')
        primeiro += razao

numero = int(input('\nDigite quantos termos a mais quer ver: '))
while numero != 0:
    decimo = decimo + razao
    print(decimo)
    numero = numero - 1

#TAMO FICANDO BOM PORRA!