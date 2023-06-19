"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(* numbers):
    count = maior = 0
  
    print('Analisando os valores passados...')
    print(f'{"-=" * 20}')
  
    for valor in numbers:
        print(f'{valor} ', end='')
     
        if count == 0:
            maior = valor
       
        else:
            if valor > maior:
                maior = valor
      
        count += 1
   
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    


# main code
maior(2, 9, 4, 5, 7, 1)
maior(4, 8 , 9)
maior(1, 2)
maior(7)
maior()