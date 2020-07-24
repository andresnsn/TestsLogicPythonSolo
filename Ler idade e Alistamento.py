from datetime import date
anoatual = date.today().year
anonasc = int(input('Digite o seu ano de nascimento: '))
if anoatual - anonasc < 18:
    print('Você ainda irá se alistar ao serviço militar! ')
    print('Restam {} anos para você se alistar no exército! '.format(18-(anoatual-anonasc)))
elif anoatual - anonasc == 18:
    print('É hora de você se alistar! ')
elif anoatual - anonasc > 18:
    print('Já passou do seu tempo de se alistar! ')
    print('Você está {} anos atrasado! '.format((anoatual-anonasc)-18))

