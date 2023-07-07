"""
Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""
def ajuda(comando):
    help(comando)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biclioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo('ATÉ LOGO!')
