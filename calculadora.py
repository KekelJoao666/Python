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
    else:
        return "Erro: divisão por zero"

while True:
    print('-------------------------------')
    print('Calculadora')
    print('-------------------------------')
    print('[1] Soma')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    print('[0] Sair')
    print('-------------------------------')

    operação = int(input('Qual equação você deseja fazer? '))

    if operação == 0:
        print('Encerrando a calculadora.')
        break  # Sai do laço

    if operação not in [1, 2, 3, 4]:
        print('Opção inválida. Tente novamente.')
        continue

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

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

    print('-------------------------------')
    print('Resultado')
    print('-------------------------------')
    print(f'Equação: {equação}\nResultado: {total}')
    print('-------------------------------\n')
