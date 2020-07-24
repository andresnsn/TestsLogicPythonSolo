num = 0
contador = 0
soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        contador += 1
        soma += num
    else:
        print('O total de números lidos foi {} e a soma destes números é {}'.format(contador, soma))



