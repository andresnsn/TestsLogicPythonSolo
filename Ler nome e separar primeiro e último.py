nome = input('Digite o seu nome: ').strip()
separado = nome.split()
print('O seu primeiro nome é: {}'.format(separado[0]))
print('O seu último nome é: {}'.format(separado[len(separado)-1]))
