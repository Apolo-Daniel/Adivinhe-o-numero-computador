def cabecalho():
  print('-' * 64)
  print('JOGO DA ADIVINHAÇÃO'.center(64))
  print('-' * 64)
  print('O Computador escolheu um número entre 1 e 10, tente adivinhá-lo!'.center(64))
  print('-' * 64)

def erro(msg):
  print(f'\033[1:31m{msg}\033[m')
  print('-' * 64)
