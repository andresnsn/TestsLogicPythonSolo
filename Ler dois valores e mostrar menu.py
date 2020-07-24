from time import sleep

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''    [1]Somar
    [2]Multiplicar
    [3]Maior Valor
    [4]Novos números
    [5]Sair do programa'''))

    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('O produto entre {} e {} é igual a {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('Entre {} e {}, o maior valor é {}'.format(num1, num2, num1))
        elif num2 > num1:
            print('Entre {} e {}, o maior valor é {}'.format(num1, num2, num2))
        elif num1 == num2:
            print('Os números são iguais!')
    elif opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao >= 6:
        print('Opção inválida, tente novamente!')
        sleep(2)
print('Finalizando programa...')
