"""
Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

def vote(age=0):
    from datetime import date
    current_year = date.today().year
    current_age = current_year - age
    
    if current_age < 16:
        return f'At {current_age} years old: DOES NOT VOTE.'
    
    elif 16 <= current_age < 18 or current_age > 70:
        return f'At {current_age} years old: OPTIONAL VOTE.'
    
    else:
        return f'At {current_age} years old: MANDATORY VOTE.'

birth_year = int(input('What year were you born? '))
print(vote(birth_year))

