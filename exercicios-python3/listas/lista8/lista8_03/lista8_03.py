vogal = ("a","e","i","o","u")
with open("lista8_03.txt","r") as arquivo:
    conteudo = arquivo.read()
    for x in range(len(conteudo)): 
        if conteudo[x] in vogal : numerovoga += 1
        if conteudo[x] in alfabeto : numeroalga += 1
    print(numeroalga,numerovoga)