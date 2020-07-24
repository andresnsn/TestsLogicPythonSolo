from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    anonasc = int(input('Digite seu ano de nascimento: '))
    if ano - anonasc >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade'.format(maior, menor))
