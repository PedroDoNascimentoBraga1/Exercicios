a,b = 0,1
for _ in range(int(input('Informe o número da sequencia: '))):
    a,b = a + b , a
    print(a)