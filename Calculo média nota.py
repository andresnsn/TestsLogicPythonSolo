nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if (nota1+nota2)/2 >= 7:
    print('Você está aprovado!')
elif (nota1+nota2)/2 >= 5 and (nota1+nota2)/2 <= 6.9:
    print('Você está de recuperação!')
else:
    print('Você está reprovado!')
