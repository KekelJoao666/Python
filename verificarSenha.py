def verificarSenha(txt):
    temLetra = False
    temNumero = False

    for c in txt:
        if c.isalpha():
            temLetra = True
        if c.isdigit():
            temNumero = True

    if not temLetra:
        print('Senha precisa ter pelo menos 1 letra.')
        return False
    if not temNumero:
        print('Senha precisa possuir ter pelo menos 1 numero.')
        return False
    else: 
        return True

while True:
    senha = str(input('Escreva uma senha: '))

    if verificarSenha(senha):
        print('Senha valida.')
        break
    else: 
        print('Senha invalida.')
