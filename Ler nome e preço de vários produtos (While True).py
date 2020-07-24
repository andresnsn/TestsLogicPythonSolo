total = cont = barato = caro = 0
nomecaro = nomebarato = ''

while True:
    opcao = ''
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    if barato == 0:
        barato = preco
    if caro == 0:
        caro = preco
    if preco < barato:
        nomebarato = produto
        barato = preco
    if preco > caro:
        nomecaro = produto
        caro = preco

    total += preco

    if preco > 1000:
        cont += 1
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Deseja continuar? ')).upper().strip()
        if opcao == 'N':
            print(f'O valor total da compra foi R${total}')
            print(f'A quantidade de produtos superiores a R$ 1000 é {cont}')
            print(f'O produto mais caro foi {nomecaro} e custou {caro}')
            print(f'O produto mais barato foi {nomebarato} e custou {barato}')
            break


