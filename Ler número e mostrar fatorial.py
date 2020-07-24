num = int(input('Digite um número: '))
multiplicador = num-1

produto = num * multiplicador

while multiplicador > 1:
    multiplicador -= 1
    produto = produto * multiplicador

print(produto)

