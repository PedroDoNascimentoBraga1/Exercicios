# Formação automática de um triângulo retângulo com o input da base do mesmo.
# Aplicação de input, laços de repetições, tranformação de stg em int, contadores e lógica de programação



base = int(input("Informe o número de asteristicos que haverá na base do triângulo: "))

cont = 0
while cont < base + 1:
    print(" * " * cont)
    cont += 1