# Calculadora

def som(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else: return

# Tipos de equações definido em um def, basicamente é a função do visualg

print('-------------------------------')
print('Calculadora')
print('-------------------------------')
print('[1] Soma')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] Divisão')
print('-------------------------------')

# Estrutura da calculadora

operação = int(input('Qual equação você deseja fazer? '))
num1 = float(input('Digite o primeiro número. '))
num2 = float(input('Digite o segundo número. '))

# Definindo variáveis 

if operação == 1:
    total = som(num1, num2)
    equação = f'{num1} + {num2}'
elif operação == 2:
    total = sub(num1, num2)
    equação = f'{num1} - {num2}'
elif operação == 3:
    total = multi(num1, num2)
    equação = f'{num1} * {num2}'
elif operação == 4:
    total = div(num1, num2)
    equação = f'{num1} / {num2}'
else: print('Erro:', NameError)

# Codando a calculadora ( conferir se o NameError faz realmente o que eu to pensando )

print('-------------------------------')
print('Resultado')
print('-------------------------------')
print(f'Equação: {equação}\nResultado: {total}')
print('-------------------------------')