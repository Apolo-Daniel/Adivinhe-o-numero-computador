from random import randint
from Textos import *
from time import sleep

tentativas = 1
Jogador = 0
cabecalho()

while True:
    Computador = randint(1, 10)
  
    while Jogador != Computador:
        try:
            Jogador = int(input('Qual é o seu palpite? '))
        except (ValueError, TypeError):
            erro('ERRO! Digite um número inteiro válido')
            continue
        else:

            if Jogador > 10 or Jogador < 1:
                erro('Digite um número inteiro entre 1 e 10')
                continue
            else:
       
                if Jogador > Computador:
                    erro('Tente um número mais baixo!')
                    tentativas += 1
                    continue
          
                elif Computador > Jogador:
                    erro('Tente um número mais alto!')
                    tentativas += 1
                    continue
          
                else:
                    print(f'Parabéns!! Você acertou o número com {tentativas} tentativas.')
                    opc = str(input('Quer continuar? [S/N] ')).lower()[0]
          
                    while opc not in 'sn':
                        erro('Erro! Digite um opção válida!')
                        opc = str(input('Quer continuar? [S/N] '))
  
                    if opc == 'n':
                        print('Até logo...')
                        sleep(1)
                        quit()
  
                    if opc == 's':
                        print('-' * 64)
                        tentativas = 1
                        continue
