"""Um código que receba um numeral e devolva-o em ordem numérica do menor para o maior"""

#conceitos trabalhados, conhecimento de array, conhecimento de variáveis, conhecimento de funções, conhecimento de laços for de repetição e conhecimentos de testes lógicos

numeral = list(input('Informe um numeral: '))

for cont in range (len(numeral)): numeral[cont] = int(numeral[cont])

for cont0 in range (len(numeral)):
    for cont1 in range (len(numeral)):
        if numeral[cont0] < numeral [cont1]:
            numeral[cont0] , numeral [cont1] =  numeral [cont1] , numeral[cont0]
print(numeral)