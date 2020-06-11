def addOne(x):
    return x+1

grafo = [[2],
        [1,2],
        [1,3,4,5],
        [5],
        [7],
        [5,7,8],
        [7],
        [6,7,8],
        [8]]

n = 9
d = -10

file = open("temp.txt",'w')
lineA = "X: {}\n"
lineNA = "Na: {}\n"
lineD = "La deficiencia es: {}\n"


for i in range((1<<n) + 1):   
    NA = []
    A = []
    for j in range(n):
        if (( i & ( 1 << j )) != 0 ):
            A.append(j)
            for vecino in grafo[j]:
                if(vecino not in NA):
                    NA.append(vecino)
    d = max(d,(len(A) - len(NA)))
    if(len(A) > 0):
        file.write(lineA.format(list(map(addOne,A))))
        file.write(lineNA.format(NA))
        file.write(lineD.format((len(A) - len(NA))))
        file.write("-"*20+"\n")
    
print(d)
file.close()
