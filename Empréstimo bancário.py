casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos você pretende pagar? '))

anos = anos*12
prestacao = casa/anos

if prestacao > salario * 0.3:
    print('Empréstimo negado! O valor da parcela é {:.2f} e 30% do seu salário é {:.2f}'.format(prestacao, salario *0.3))
else:
    print('Ok, empréstimo concedido! O valor da parcela é {:.2f} e 30% do seu salário é {:.2f}'.format(prestacao, salario *0.3))
