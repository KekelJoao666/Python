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

