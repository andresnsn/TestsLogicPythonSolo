km = float(input('Qual a distância da viagem? '))

if km <= 200:
    print('Sua viagem custou R$ {:.2f} '.format(km*0.50))
else:
    print('Sua viagem custou R$ {:.2f} '.format(km*0.45))
