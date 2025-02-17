numcor= []
for i in range (int(input("Inicio: "))):
    entrada = int(input("entrada: "))
    numcor.pop(len(numcor) - 1) if (entrada) == 0  else numcor.append(entrada)
resposta = 0
for i in range(len(numcor)): resposta += numcor[i]
print(resposta)