def lin(a):
    for i in range (0,a):
        print('\\\\'+'-'*60+'//')

lin(2)
print (25*' ' + 'CALCULADORA')
print(10*' ' + '**Após cada passo precione enter**')
print(10*' ' + '** Pare digitando <0>* *')
print(10*' ' + ' 1 - Informe um número**')
print(10*' ' + ' 2 - Informe uma operação**')
lin(2)
print('Inicio: ')

resto = entrada = int(input("informe um número:"))
while True :
    operação = input("Informe uma operação:")
    entrada = int(input("informe um número:"))
    if operação == "x":
        resto *= entrada
    elif operação == "/":
        resto /= entrada
    elif operação == "+":
        resto += entrada
    elif operação == "-":
        resto -= entrada
    print("resultado atual: " , resto)
    if operação == 0 or entrada == 0:
        break
