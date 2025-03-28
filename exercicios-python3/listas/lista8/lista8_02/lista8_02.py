vogal = ("a","e","i","o","u")
alfabeto = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
with open("lista8_02.txt","r") as arquivo:
    conteudo = arquivo.read()
    numeroalga = 0
    numerovoga= 0
    for x in range(len(conteudo)): 
        if conteudo[x] in vogal : numerovoga += 1
        if conteudo[x] in alfabeto : numeroalga += 1
    print(numeroalga,numerovoga)