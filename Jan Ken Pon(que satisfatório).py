import random
from time import sleep
lista = ['papel', 'pedra', 'tesoura']
computador = random.choice(lista)
print('\033[1;32mVamos jogar Jan Ken Pon! Pressione uma tecla para continuar...\033[m')
input()
print('\033[1;30mCarregando...\n\033[m')
sleep(1)
jogador = str(input('\033[1;37;48mVamos ver se você é o bichão memo! Digite Pedra, Papel ou Tesoura!\n \033[m')).lower().strip()

print('\033[1;34mJAN!\033[m')
sleep(0.5)
print('\033[1;33mKEN!\033[m')
sleep(0.5)
print('\033[1;31mPON!\033[m')
 
# Opção inválida

while jogador != 'pedra' and jogador != 'tesoura' and jogador != 'papel':
        print('\033[1;30mQual foi mano, opção inválida! Tá tentando fugir? ( ͡° ͜ʖ ͡°)\033[m')
        break

# Jogador escolhe Pedra

if jogador == 'pedra' and computador == 'tesoura':
    print('\033[1;37mPorra, você me venceu! Eu escolhi\033[m {}{}{}'.format('\033[1;31m', computador.upper(), '\033[m'))
elif jogador == 'pedra' and computador == 'papel':
    print('\033[1;37mToma otário, Eu escolhi\033[m {}{}{}'.format('\033[1;33m', computador.upper(), '\033[m'))
elif jogador == 'pedra' and computador == 'pedra':
    print('\033[1;37mIh, deu empate! Eu escolhi\033[m {}{}{} também! '.format('\033[1;34m', computador.upper(), '\033[m'))

# Jogador escolhe Tesoura

elif jogador == 'tesoura' and computador == 'papel':
    print('\033[1;37mKarai viado, ganhou essa! Eu escolhi\033[m {}{}{}'.format('\033[1;31m', computador.upper(), '\033[m'))
elif jogador == 'tesoura' and computador == 'pedra':
    print('\033[1;37mIrrraaaa, tomou no cu kkkkkkk! Escolhi\033[m {}{}{}'.format('\033[1;34m', computador.upper(), '\033[m'))
elif jogador == 'tesoura' and computador == 'tesoura':
    print('\033[1;37mÉ, empatamos. Again! Eu escolhi {}{}{} também!\033[m'.format('\033[1;31m', computador.upper(), '\033[m'))

# Jogador escolhe Papel

elif jogador == 'papel' and computador == 'pedra':
    print('\033[1;37mMerda, te subestimei! Eu escolhi {}{}{}... Go outra!\033[m'.format('\033[1;34m', computador.upper(), '\033[m'))
elif jogador == 'papel' and computador == 'tesoura':
    print('\033[1;37mReceba filho do cabrunco! Ganhei! Pickei\033[m {}{}{}'.format('\033[1;31m', computador.upper(), '\033[m'))
elif jogador == 'papel' and computador == 'papel':
    print('\033[1;37mÉ, empatamos... Escolhi\033[m {}{}{}!'.format('\033[1;33m', computador.upper(), '\033[m'))
