# ✅ Funções auxiliares (usadas em várias questões)

def somenteLetra(txt):
    return txt.replace(" ", "").isalpha()

def somenteNumero(num):
    return num.isdigit()

def negativoPositivo(num):
    return num >= 0

def imparPar(num):
    return num % 2 == 0

def maiorMenor(num1, num2):
    return num1 > num2

def multiploDe(num1, num2):
    return num1 % num2 == 0

def intervalo(num1):
    return 1 <= num1 <= 100

def verificarEndereco(txt):  # ✅ Questão 12
    if txt in ['SP', 'RJ', 'MG']:
        return 'Sudeste'
    elif txt in ['RS', 'SC', 'PR']:
        return 'Sul'
    else:
        return 'Outra região'

def positivoSoma(num1, num2):  # ✅ Questão 13
    if negativoPositivo(num1) and negativoPositivo(num2):
        return num1 + num2
    else:
        return "Números inválidos."

def divisivelTres(num):  # ✅ Questão 14
    return num % 3 == 0 or num % 5 == 0

def verificarInicial(txt):  # ✅ Questão 15
    return txt[0].lower() == 'a'

def maiorMenorIgual(num1, num2):  # ✅ Questão 4 e 10
    if num1 > num2:
        return 'O primeiro número é maior que o segundo.'
    elif num1 == num2:
        return 'O primeiro número é igual ao segundo.'
    else:
        return 'O primeiro número é menor que o segundo.'

def verificarSenha(txt):  # ✅ Questões 10 e 18
    if len(txt) < 6:
        print('A senha precisa ter pelo menos 6 dígitos.')
        return False

    temLetra = any(c.isalpha() for c in txt)
    temNumero = any(c.isdigit() for c in txt)

    if not temLetra:
        print('Senha precisa possuir pelo menos 1 letra.')
    if not temNumero:
        print('Senha precisa possuir pelo menos 1 número.')

    return temLetra and temNumero

def verificarPrimo(num):  # ✅ Questão 19
    if num < 2:
        return False
    for c in range(2, int(num ** 0.5) + 1):
        if num % c == 0:
            return False
    return True

# ✅ Questões 3, 6, 9, 10, 11, 17 — Coleta e validação dos dados do usuário

while True:
    print('\nLOGIN\n')

    nome = input('Digite o seu nome: \n')
    if not somenteLetra(nome):
        print('Digite APENAS letras.')
        continue
    print(f'O nome \"{nome.title()}\" foi registrado!')

    telefone = input('Digite seu número de telefone: \n')
    if not somenteNumero(telefone):
        print('Digite APENAS números.')
        continue
    if not 8 <= len(telefone) <= 12:
        print('O número precisa conter de 8 a 12 dígitos.')
        continue
    telefoneFormatado = f'({telefone[:2]}) {telefone[2]} {telefone[3:7]}-{telefone[7:]}'
    print(f'O telefone \"{telefoneFormatado}\" foi registrado!')

    idade = input('Digite a sua idade: \n')
    if not somenteNumero(idade):
        print('Digite APENAS números.')
        continue
    idade = int(idade)
    if not negativoPositivo(idade):
        print('Digite APENAS números positivos.')
        continue
    print(f'A idade \"{idade}\" foi registrada.')

    cidade = input('Digite o nome da sua cidade: \n').title()
    if not somenteLetra(cidade):
        print('Digite APENAS letras.')
        continue
    print(f'A cidade \"{cidade}\" foi registrada.')

    senha = input('Escreva uma senha de 6 dígitos com ao menos 1 letra e 1 número: \n')
    if not verificarSenha(senha):
        continue

    print('Senha válida!\n')
    print(f'Seja bem-vindo(a) {nome.title()}, seu login está completo!')

    infoPessoais = {
        'nome': nome,
        'idade': idade,
        'telefone': telefoneFormatado,
        'cidade': cidade,
        'senha': senha
    }
    break

# ✅ Menu principal (1 a 20)

while True:
    try:
        continuar = int(input('\n[0] Sair\n[1] Positivo/Negativo\n[2] Par/Ímpar\n[3] Maior número\n[4] Múltiplo\n[5] Intervalo 1–100\n[6] Soma se positivos\n[7] Divisível por 3 ou 5\n[8] Maior/Menor entre 3 números\n[9] Primo\n[10] Comparar dois números\n[11] Começa com A?\n[12] Apenas letras?\n[13] Contar caracteres\n[14] Sigla do estado\n[15] Exibir perfil\n[20] Buscar preço de produto\n> '))
    except ValueError:
        print('Digite apenas números válidos.')
        continue

    if continuar == 0:
        break

    if continuar <= 10 or continuar == 19:
        num1 = input('\nDigite um número: ')
        if not somenteNumero(num1):
            print('Digite apenas números.')
            continue
        num1 = float(num1)

    if continuar >= 11 and continuar <= 13 or continuar == 15:
        txt = input('\nDigite uma palavra ou frase: ')
        if not somenteLetra(txt):
            print('Digite apenas letras.')
            continue

    # ✅ Questão 1
    if continuar == 1:
        print(f'O número {num1} é positivo.' if negativoPositivo(num1) else f'O número {num1} é negativo.')

    # ✅ Questão 2
    if continuar == 2:
        print(f'O número {num1} é par.' if imparPar(num1) else f'O número {num1} é ímpar.')

    # ✅ Questão 4
    if continuar == 3:
        num2 = input('\nDigite um segundo número: ')
        if not somenteNumero(num2):
            print('Digite apenas números.')
            continue
        num2 = float(num2)
        print(f'O primeiro número {num1} é maior.' if maiorMenor(num1, num2) else f'O segundo número {num2} é maior.')

    # ✅ Questão 5
    if continuar == 4:
        num2 = input('\nDigite um segundo número: ')
        if not somenteNumero(num2):
            print('Digite apenas números.')
            continue
        num2 = float(num2)
        print(f'{num1} é múltiplo de {num2}.' if multiploDe(num1, num2) else f'{num1} não é múltiplo de {num2}.')

    # ✅ Questão 8
    if continuar == 5:
        print(f'{num1} está entre 1 e 100.' if intervalo(num1) else f'{num1} não está entre 1 e 100.')

    # ✅ Questão 13
    if continuar == 6:
        num2 = input('\nDigite o segundo número: ')
        if not somenteNumero(num2):
            print('Digite apenas números.')
            continue
        num2 = float(num2)
        print(positivoSoma(num1, num2))

    # ✅ Questão 14
    if continuar == 7:
        print(f'{num1} é divisível por 3 ou 5.' if divisivelTres(num1) else f'{num1} não é divisível por 3 ou 5.')

    # ✅ Questão 16
    if continuar == 8:
        num2 = input('\nDigite o segundo número: ')
        num3 = input('Digite o terceiro número: ')
        if not (somenteNumero(num2) and somenteNumero(num3)):
            print('Digite apenas números.')
            continue
        num2 = float(num2)
        num3 = float(num3)
        lista = [num1, num2, num3]
        print(f'Maior: {max(lista)}, Menor: {min(lista)}')

    # ✅ Questão 19
    if continuar == 9:
        print(f'{num1} é primo!' if verificarPrimo(num1) else f'{num1} não é primo.')

    # ✅ Questão 10
    if continuar == 10:
        num2 = input('Digite o segundo número: ')
        if not somenteNumero(num2):
            print('Digite apenas números.')
            continue
        num2 = float(num2)
        print(maiorMenorIgual(num1, num2))

    # ✅ Questão 15
    if continuar == 11:
        print('Começa com "A".' if verificarInicial(txt) else 'Não começa com "A".')

    # ✅ Questão 6
    if continuar == 12:
        print('Apenas letras!' if somenteLetra(txt) else 'Contém outros caracteres.')

    # ✅ Questão 7
    if continuar == 13:
        print(f'A frase possui {len(txt)} caracteres.')

    # ✅ Questão 12
    if continuar == 14:
        estado = input('Digite a sigla do estado (ex: SP): ').upper()
        print(verificarEndereco(estado))

    # ✅ Questão 17
    if continuar == 15:
        print('\n--- PERFIL ---')
        for chave, valor in infoPessoais.items():
            print(f'{chave.title()}: {valor}')

    # ✅ Questão 20
    if continuar == 20:
        produtos = {
            'arroz': 5.49,
            'feijão': 6.79,
            'açúcar': 4.29,
            'café': 12.50,
            'óleo': 7.39
        }
        print('\nProdutos disponíveis:', ', '.join(produtos.keys()))
        item = input('Digite o nome do produto: ').lower()
        if item in produtos:
            print(f'O preço do produto "{item}" é R$ {produtos[item]:.2f}')
        else:
            print('Produto não encontrado.')
