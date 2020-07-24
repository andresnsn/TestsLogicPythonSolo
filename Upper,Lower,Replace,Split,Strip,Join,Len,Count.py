nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
separado = nome.split()
junto = ''.join(separado)
print(len(junto))
print(len(separado[0]))


#O exercício pedia para contar a quantidade de letras, sem considerar os espaços
#Fizemos então o objeto "separado" receber o objeto "nome" com o método split.
#Após splitar e transformar a String em lista, juntamos novamente com o método
# .join. O método junta, e então usamos a função len para contar a quantidade
# de letras

#Podemos também usar len(nome) - nome.count(' ').
#O método count conta os espaços e os subtrai da string, retornando o número de
#letras corretamente, sem contar os espaços.

#Pode-se usar o método strip após o parênteses do "input" para eliminar espaços
#desnecessários inseridos pelo usuário.

#print('Seu primeiro nomte tem {} letras'.format(nome.find(' '))