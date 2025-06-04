valorInicial = float(input('Quantos R$ você deseja depositar na sua poupança? '))
valorAtual = valorInicial
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8') # isso é para conseguir formatar datas, valores, etc. no padrão brasileiro

for mes in range(1, 13):
    valorAtual = valorAtual * (1 + 0.005) # vi no google que a fórmula é essa
    print(f'No {mes}º você possui {locale.currency(valorAtual, grouping=True)}') # : - inicia a formatação; .2 - limita a 2 casa decimais; f - float, num com virgula

# Erick