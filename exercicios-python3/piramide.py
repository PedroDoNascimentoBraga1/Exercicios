# Formação automática de uma pirâmide com o input da base do mesmo.
# Aplicação de input, laços de repetições, tranformação de stg em int, contadores e lógica de programação

cont = 0

base = int(input("Informe o número de asteristicos que haverá na base da pirâmide: "))

contespa = base - 1 #váriavel para contar os espaços da esquerda da pirâmide
cont = 1

while cont < base + 1:
    print("  " * contespa ,"  * " * cont)
    contespa -= 1
    cont += 1