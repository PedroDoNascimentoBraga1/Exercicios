a = float(input("A :"))
b = float(input("B :"))
c = -999999998
while True:
    media = (a + b + c) / 3
    mediana = [c,a,b]
    mediana.sort()
    meana = mediana[(len(mediana) // 2) ]
    if media == meana: break 
    else: c += 1
print(c)