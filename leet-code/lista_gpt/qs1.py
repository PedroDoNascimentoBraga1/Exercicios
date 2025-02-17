inp1 = input("Input 1 : ").lower()
inp2 = input("Input 2 : ").lower()
print("É anagrama") if sorted(inp1) == sorted(inp2) else print("Não é um anagrama")