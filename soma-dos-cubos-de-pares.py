while True:
    numInicio = int(input('Digite o numero de inicio: '))
    numFinal = int(input('Digite o numero de final: '))

    if numFinal > numInicio:
        break
    print('\nO numero inicial precisa ser menor que o final. Tente novamente\n')

# Cria um laço que impede que o código rode caso numInicio seja maior que numFinal

paresCubo = []
soma = 0

for i in range(numInicio + 1, numFinal):
    if i % 2 == 0:
        paresCubo.append(i**3)
print(f'{paresCubo}\n\n{sum(paresCubo)}')

# Erick
