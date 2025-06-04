base = int(input('Escreva um numero para ser a base. '))
expoente = int(input('Escreva um numero para ser a expoente. '))
resultado = 1

for i in range(1, expoente + 1):
    resultado = resultado * base
print(resultado)