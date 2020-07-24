print('Velocidade máxima permitida: 80km/h')
velocidade = float((input('Qual a velocidade do carro? ')))

if velocidade > 80:
    print('Você foi multado. O valor da sua multa é: R$ {} '.format((velocidade-80)*7))

else:
    print('Parabéns, você está dentro do limite de velocidade! ')
