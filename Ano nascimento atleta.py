from datetime import date
anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
if anoatual - anonasc <= 9:
    print('\033[4;33;46mVocê é MIRIM! \033[m')
elif anoatual-anonasc <= 14:
    print('Você é INFANTIL')
elif anoatual-anonasc <= 19:
    print('Você é JUNIOR! ')
elif anoatual-anonasc <= 20:
    print('Você é SÊNIOR! ')
else:
    print('Você é MASTER! ')
