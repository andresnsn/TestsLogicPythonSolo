num = 1
soma = 0
c = 0
maior = 0
menor = 0
while num != 0:
    num = int(input('Digite um número: '))
    soma += num
    if num != 0:
        c += 1
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    if num != 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média de todos os números foi {}'.format(soma/c))
print('O maior valor lido foi {} e o menor {}'.format(maior, menor))

