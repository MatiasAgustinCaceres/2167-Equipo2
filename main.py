from matias_agustin_caceres.Matriz_3x3 import *

print("Hola mundo")

c = Matriz_3x3 (1,2,3,4,5,6,7,8,9)
a = Matriz_3x3 (1,2,3,4,5,6,7,8,9)

for i in range(3):
    for j in range (3):
        print (c.matriz[i][j])
                

c.suma(a)


for i in range(3):
    for j in range (3):
        print (c.matriz[i][j])