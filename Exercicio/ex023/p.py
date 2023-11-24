numero1 = str(input('Digite um numero: '))
numero2 = str(input('Digite outro numero: '))

if (numero1.isnumeric() and numero2.isnumeric()):
    numero1, numero2 = int(numero1), int(numero2)
    soma = numero1 + numero2
    print(f'A soma entre {numero1} + {numero2} = {soma}')

else:
    if (numero1.isalpha() or numero2.isalpha()):
        print('Digite apenas valores númericos')


    if (numero1.isspace() and numero2.isspace()):
        print('Você digitou apenas espaço')
        print('Tente novamente')
        
    # if (numero1.isalnum() or numero2.isalnum()):
    #     print('Você digitou um valor numerico e letra')
    #     print('Tente novamente')

print('Fim do programa')

