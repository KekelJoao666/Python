print('ATIVIDADES PYTHON\nALUNO:JOÃO PEDRO BARRETO')
print('\nExercícios diretos e de única validação:')
#
print('\n1. Peça ao usuário um número e informe se ele é positivo ou negativo.')
numero=int(input('Escreva seu número: '))
if numero > 0:
    pon='positivo'
if numero < 0:
    pon='negativo'
print(f'Seu número é: {pon}')
#
print('\n2. Peça um número e informe se ele é par ou ímpar.')
numero=int(input('Escreva seu número: '))
if numero % 2 == 0:
    poi='par'
else:
    poi='ímpar'
print(f'Seu número é {poi}')
#
print('\n3. Peça ao usuário seu nome e diga: "Olá, [nome]".')
nome=input('Qual seu nome? ')
print(f'Olá {nome}')
#
print('\n4. Peça dois números e informe se o primeiro é maior, menor ou igual ao segundo.')
num1=int(input('Escreva o primeiro número: '))
num2=int(input('Escreva o segundo número: '))

