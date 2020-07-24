s = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            cont = cont + 1
            s = s + c
print('A soma de todos os valores ímpares e múltiplos de 3, que são um total de {}, números  até 500, é {}'.format(cont, s))

#Nós adicionamos "cont" depois de ver a resolução do Guanabara, como um adicional.
# Neste caso, nós acertamos o exercício, mas o Guanabara propôs que o programa também contasse
# a quantidade de números que o programa encontrou, que atendem as condições, e que foram somados.
