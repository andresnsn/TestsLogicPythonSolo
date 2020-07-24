cont = 0
masc = 0
femi = 0
opcao = ''

while True:
    opcao = ''
    sexo = ''
    idade = ''
    verdadeiro = False
    while verdadeiro == False:
        idade = str(input('Qual a sua idade? '))
        verdadeiro = idade.isnumeric()
        if verdadeiro == True:
            idade = int(idade)
            if idade >= 18:
                cont += 1


    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Qual seu sexo (M/F)?  ')).upper().strip()
        if sexo != 'M' and sexo != 'F':
            print('Valores inválidos, digite novamente! ')


    if sexo == 'M':
        masc += 1
    if sexo == 'F':
        if idade < 20:
            femi += 1

    while opcao != 'N' and opcao != 'S':
        opcao = str(input('Deseja continuar cadastrando (S/N)? ')).upper().strip()

    if opcao == 'N':
        print('Finalizando...')
        break

print(f'No total, foram cadastradas {cont} pessoas maiores de 18 anos. ')
print(f'No total, também foram cadastrados {masc} homens.')
print(f'Por fim, a quantidade de mulheres com menos de 20 anos é {femi}.')


