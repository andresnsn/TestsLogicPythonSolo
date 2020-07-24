from time import sleep
produto = float(input('Digite o preço do produto: '))
print('Carregando formas de pagamento...')
sleep(3)
opcao = int(input('Digite:\n1- À vista/cheque\n2- À vista/cartão\n3- 2x no cartão\n4- 3x ou mais no cartão\n'))
if opcao == 1:
    print('O preço do produto receberá 10% de desconto: R$ {}'.format(produto*0.9))
elif opcao == 2:
    print('O preço do produto receberá 5% de desconto: R$ {}'.format(produto*0.95))
elif opcao == 3:
    print('O preço do produto ficará igual ao original: R$ {}'.format(produto))
else:
    print('O produto sofrerá um adicional de 20% de juros: R$ {}'.format(produto*1.2))

