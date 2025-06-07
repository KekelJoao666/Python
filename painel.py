def verificarLetra(texto):
    if texto.isalpha():
        return True
    else:
        return False

def verificarNumero(num):
    if num.isdigit():
        return True
    else:
        return False

def negativoPositivo(num):
    if num >= 0:
        return True
    else:
        return False
    
def imparPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def maiorMenor(num1, num2):
    if num1 > num2:
        return True
    else:
        return False
    
def múltiploDe(num1, num2):
    if num1 > num2:
        return True
    else:
        return False
    
def intervalo(num1):
    if num1 >= 1 and num1 <= 100:
        return True
    else:
        return False
    
def verificadorLetras(txt):
    if txt.isalpha():
        return True
    else:
        return False

def verificarSenha(txt):
    if len(txt) < 6:
        print('A senha precisa ter pelo menos 6 dígitos.')

    temLetra = False
    temNumero = False

    for c in txt:
        if c.isalpha():
            temLetra = True
        if c.isdigit():
            temNumero = True

    if not temLetra:
        print('Senha precisa possuir pelo menos 1 letra.')
        return False
    if not temNumero:
        print('Senha precisa possuir pelo menos 1 numero.')
        return False
    else: 
        return True
    
while True:
    print('\nLOGIN\n')

    nome = str(input('Digite o seu nome: '))
    
    if not verificarLetra(nome):
        print('Digite APENAS letras.')

    idade = input('Digite o sua idade: ')

    if not verificarNumero(idade):
        print('Digite APENAS números.')
    else: 
        idade_int = int(idade)

    if not negativoPositivo(idade_int):
        
        print('Digite APENAS números positivos.')

    senha = str(input('Escreva uma senha de 6 dígitos com ao menos 1 letra e ao menos 1 número: '))

    if verificarSenha(senha):
        print('Senha válida!\n')
        print(f'Seja bem-vindo(a) {nome.title()}, seu login está completo!') 
        break   


while True:
    
    try:
        continuar = int(input('\n[ 1 ] Negativo ou Positivo\n[ 2 ] Impar ou Par\n[ 3 ] Qual numero é maior?\n[ 4 ] Múltiplos\n[ 5 ] Intervalo de 1 a 100\n[ 6 ] Essa palavra possui apenas letra?\n[ 7 ] Contador de caracteres\n[ 0 ] Parar\n'))
    except ValueError:
        print('Digite apenas números válidos para o menu.')
        continue

    if continuar == 0: 
        break
    elif continuar > 7:
        print('Digite um dos números presentes na lista.')
        continue

    if continuar <= 5:
        num1 = float(input('\nDigite um numero qualquer: \n'))
    else:
        texto = str(input('\nDigite uma palavra ou frase: \n'))

    if continuar == 1: # Verifica se é negativo ou positivo ( exercício 1 )
        if negativoPositivo(num1):
            print(f'\nO numero {num1} é: positivo!')
        else:
            print(f'O numero {num1} é: negativo!')

    if continuar == 2:
        if imparPar(num1):
            print(f'\nO numero {num1} é: par!')
        else:
            print(f'\nO numero {num1} é: impar!')

    if continuar == 3:
        num2 = float(input('\nDigite um segundo numero qualquer: '))

        if maiorMenor(num1, num2):
            print(f'\nO primeiro numero {num1} é maior que o segundo numero {num2}!')
        else:
            print(f'\nO segundo numero {num2} é maior que o primeiro numero {num1}!')
    
    if continuar == 4:
        num2 = float(input('\nDigite um segundo numero qualquer: '))

        if múltiploDe(num1, num2):
            print(f'O numero {num1} É múltiplo do numero {num2}!')
        else:
            print(f'O numero {num1} NÃO É múltiplo do numero {num2}!')

    if continuar == 5:
        if intervalo(num1):
            print(f'O numero {num1} está entre 1 a 100.')
        else:
            print(f'O numero {num1} NÃO está entre 1 a 100.')

    if continuar == 6:
        if verificadorLetras(texto):
            print(f'A palavra \"{texto}\" possui APENAS letras!')
        else:
            print(f'A palavra \"{texto}\" NÃO possui apenas letras!')

    if continuar == 7:
        print(f'Sua frase possui {len(texto)} caracteres!')
