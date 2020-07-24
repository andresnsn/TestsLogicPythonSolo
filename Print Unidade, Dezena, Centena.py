numero = int(input('Digite um número de 0 a 9999: '))
u = numero % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}\n'.format(u, d, c, m))
