# Abrindo o arquivo para leitura
with open("lista8_01.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    print(len(conteudo))
