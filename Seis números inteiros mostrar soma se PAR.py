s = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('Eu achei {} números pares e a soma deles foi {}'.format(cont, s))

#Adicionar um contador para ficar bacana, exemplo cont = 0 e adiciona abaixo de "s".
#Assim o programa vai testar os valores e informar quantos números pares ele achou.