frase = str(input('Digite uma frase: ')).lower()
lista = frase.split()
junto = ''.join(lista)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Esta palavra é um palíndromo!')
else:
    print('Esta palavra não é um palíndromo!')

# Para realizar em FOR, teríamos que fazer ele contar da última à primeira letra e
# armazenar isto em uma variável. O FOR contou a partir da última letra (fun LEN).
# A variável inverso, somada a ela mesma, foi armazenando cada letra contada
#inversamente no laço, até terminar. No fim, a variável inverso possuía a palavra
# completamente invertida, então comparamos no final com if.

# Também podemos fazer muito mais facilmente, eliminando este FOR e fazendo o seguinte:
# inverso = junto[::-1]
# Notar que, sempre que em colchetes, indica uma posição na string ou lista.
# Quando não há valores entre o primeiro e segundo ":", o Python entende
# que a posição será do início ao fim. O último valor, como sabemos, é para indicar
# a razão ou casas que irá pular na posição. Como estamos com -1 no posicionamento,
# ele continua inversamente.