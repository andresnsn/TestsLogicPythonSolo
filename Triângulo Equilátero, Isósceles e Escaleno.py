print('Este programa informa se é possível criar um retângulo com o valor de 3 retas! ')
reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Essas retas podem formar um triângulo! ')
    if reta1 == reta2 == reta3:
        print('Seu triângulo é Equilátero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Seu triângulo é Isósceles')
    elif reta1 != reta2 != reta3:
        print('Seu triângulo é Escaleno!')
else:
    print('Essas retas não podem formar um triângulo!')
