salario=float(input('Escreva seu salário: '))

if salario <= 1518:
    aliquota=0.075

elif salario >1518 and salario <= 2793.88:
    aliquota=0.09

elif salario >2793.88 and salario <= 4190.83:
    aliquota=0.12

elif salario >4190.83:
    aliquota=0.14

desconto=aliquota * salario

print('O valor a ser descontado do seu salário é: ',desconto)

print('\nO valor do seu salário sem a parcela do INSS é: ',salario - desconto)
