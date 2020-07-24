salario = float(input('Digite seu salário: '))

if salario <= 1250:
    print('Seu novo salário é: R$ {:.2f}'.format(salario*1.1))
else:
    print('Seu novo salário é: R$ {:.2f}'.format(salario*1.15))
