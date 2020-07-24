sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        print('Você é do sexo masculino! ')
        break
    elif sexo == 'F':
        print('Você é do sexo feminino! ')
        break
    else:
        print('Valor inválido, digite novamente! ')

# Nice porra!