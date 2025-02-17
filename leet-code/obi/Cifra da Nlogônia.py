def cripto(coori: str):
    if coori not in vogal:
        resposta1 = coori # passo um

        resposta2 = ("a") if (alfabeto.index(coori) >= 0 and alfabeto.index(coori) <= 2) else ("e") if (alfabeto.index(coori) >= 3 and alfabeto.index(coori) <= 6) else ("i") if (alfabeto.index(coori) >= 11 and alfabeto.index(coori) <= 11) else ("o") if (alfabeto.index(coori) >= 12 and alfabeto.index(coori) <= 18) else "u" #passo dois

        resposta3 = "z" if coori == "z" else ((alfabeto[alfabeto.index(coori) + 1])) if (alfabeto[alfabeto.index(coori) + 1]) not in vogal else (alfabeto[alfabeto.index(coori) + 2]) # passo três

        return resposta1 + resposta2 + resposta3 
        
    else: return coori

alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']

vogal = ['a','e','i','o','u']

entrada = input("Informe uma palavra: ")
for i in range (len(entrada)):
    print(cripto(entrada[i]))