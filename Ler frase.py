frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print ('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))


#Adicionamos +1 no final, para que ao invés de mostrar A na posição "0"
#(no caso da palavra "André", por exemplo, ele mostra na posição "1"(lido por humanos).