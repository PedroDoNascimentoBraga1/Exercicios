'''if item[::-1] == item:return True'''

s = input("Input: ")

preredo = 0
corsda = len(s)
resado = 0
while resado == 0:
    for i in range(0,corsda):
        preredo = list(s)
        preredo.pop()
        if preredo[::-1] == preredo:
            resado = preredo
        corsda -= 1