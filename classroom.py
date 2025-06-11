print('ATIVIDADES PYTHON\nALUNO:JOÃO PEDRO BARRETO')
print('\nExercícios diretos e de única validação:')
#
print('\n1. Peça ao usuário um número e informe se ele é positivo ou negativo.')
numero=int(input('Escreva seu número: '))
if numero > 0:
    pon='positivo'
if numero < 0:
    pon='negativo'
print(f'Seu número é: {pon}.')
#
print('\n2. Peça um número e informe se ele é par ou ímpar.')
numero=int(input('Escreva seu número: '))
if numero % 2 == 0:
    poi='par'
else:
    poi='ímpar'
print(f'Seu número é {poi}.')
#
print('\n3. Peça ao usuário seu nome e diga: "Olá, [nome]".')
nome=input('Qual seu nome? ')
print(f'Olá {nome}')
#
print('\n4. Peça dois números e informe se o primeiro é maior, menor ou igual ao segundo.')
num1=(input('Escreva o primeiro número: '))
num2=(input('Escreva o segundo número: '))
if num1.isdigit and num2.isdigit:
    if num1 == num2:
        print('Os dois números são iguais.')
    else:
        if num1 > num2:
            print('O primeiro número é maior que o segundo.')
        else:
            print('O segundo número é maior que o primeiro.')
#
print('\n5. Peça ao usuário dois números e informe se eles são múltiplos entre si.')
num=int(input('Escreva o primeiro número: '))
num=int(num)
num1=int(input('Escreva o segundo número: '))
num1=int(num)

if num1 % num == 0 or num % num1 == 0:
    print('Os dois números são múltiplos de si.')
#
print('\n6. Peça uma palavra e informe se ela contém apenas letras.')
palavra=input('Escreva sua palavra: ')
if palavra.isalpha():
    print('Sua palavra contém apenas letras.')
else:
    print('Sua palavra não contém apenas letras.')
#
print('\n7. Peça ao usuário uma frase e conte quantos caracteres ela possui.')
frase=input('Escreva sua frase: ')
print(f'Sua frase tem {len(frase)} caracteres.')
#
print('\n8. Peça um número inteiro e informe se ele está no intervalo de 1 a 100.')
num=int(input('Escreva um número inteiro: '))
if num >=1 and num <=100:
    print(f'{num} está no intervalo de 1 a 100.')
else:
    print(f'{num} não está no intervalo de 1 a 100.')
#
print('\n9. Peça um nome e uma idade:\n- Nome deve conter apenas letras.\n- Idade deve ser número positivo.')
nome=input('Qual seu nome? ')
idade=input('Qual sua idade?' )

if nome.isalpha and idade.isdigit() >0:
    idade=int(idade)
    print(f'Seu nome é: {nome} e sua idade é: {idade}')
else: 
    print('Seu nome não é apenas letras e/ou sua idade não é um número')
#
print('\n10. Peça uma senha e valide:\n- Mínimo 6 caracteres.\n- Pelo menos 1 letra e 1 número.')
senha=input('Escolha uma senha: ')
aceita=False
for verifica in senha:
    if len(senha) > 6:
        if verifica.isalpha:
            if verifica.isdigit():
                aceita=True
if aceita==True:
    print('Sua senha foi aceita.')
else:
    print('Sua senha não foi aceita')
#
print('\n11. Peça um telefone:\n- Deve conter apenas números.\n- Entre 8 e 12 dígitos.')
telefone=input('Qual seu número de telefone? ')
aceita=False

if telefone.isdigit():
    if len(telefone) > 8 and len(telefone) < 12:
        aceita=True
if aceita==True:
    print('Seu número de telefone foi aceito.')
else:
    print('Seu número de telefone não foi aceito')
#
print('\n12. Peça ao usuário para informar a sigla de um estado brasileiro e valide:\n-Se for "SP", "RJ", ou "MG" → exiba: "Sudeste".\n-Se for "RS", "SC", ou "PR" → exiba: "Sul".\n-Caso contrário → exiba: "Outra região".')
sudeste=['MG', 'SP', 'RJ']
sul=['SC', 'PR', 'RS']

sigla=input('\nEscreva a sigla do seu estado: ')
sigla=sigla.upper()

if sigla in sudeste:
    print('Você é do: sudeste')
elif sigla in sul:
    print('Você é do sul.')
else:
    print('Não foi possível identificar sua região.')
#
print('\n13. Peça dois números:\n- Se ambos forem positivos → exiba a soma.\n- Se não → exiba: "Números inválidos".')
numero=input('Escreva o primeiro número: ') 
numero=float(numero)
numero1=input('escreva o segundo número: ')
numero1=float(numero1)
if numero >0 and numero1 >0:
    print(f'Resposta: {numero+numero1}')
else:
    print('Números inválidos.')
#
print('\n14. Peça um número e informe se ele é divisível por 3 ou 5.')
numero=input('Escreva seu número: ')
numero=float(numero)

if numero % 3 == 0:
    print(f'{numero} é divisível por 3')
if numero % 5 == 0:
    print(f'{numero} é divisível por 5')
#
print('\n15. Peça um texto e informe:\n- Se ele começa com a letra "A" ou "a".')
texto=input('Escreva seu texto: ')
if texto[0]=='A' or texto[0]=='a':
    a=texto[0]
    print(f'Seu texto começa com "{a}"')
#
