from teste import *
from time import sleep

def main():
    TEMPO = 1
    
    print('\nSeja bem-vinde! ')
    nome = input('Qual o seu nome? ')
    sleep(TEMPO)
    
    print(f'\nSeja bem-vinde, {nome}!')
    sleep(TEMPO)
    
    print('\nComo posso te ajudar?')
    print("""\n1 - Coxinha
2 - Pão de queijo
3 - Pastel
4 - Coca-cola""")
    
    while True:
        sleep(TEMPO)
        opcao = int(input('\nQual a sua opção? '))
        sleep(TEMPO)
        match opcao:
            case 1:
                print(f'\nO valor é {formatar_reais(3)} por coxinha.')
                break
            case 2:
                print(f'\nO valor é {formatar_reais(2)} por pão de queijo.')
                break
            case 3:
                print(f'\nO valor é {formatar_reais(5)} por pastel.')
                break
            case 4:
                print(f'\nO valor é {formatar_reais(6)} por 2 litros de coca-cola.')
                break
            case _:
                print('\nFavor, digite uma opção válida!')
                continue

main()
