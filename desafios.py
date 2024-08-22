import random
estudiante = ["Pablo", "Juan", "William", "Arco"]
materia = ["Alumno", "Algebra", "Discreta", "Prog", "Ingles"]
matriz = []

def crearmatriz():
    for fila in range(len(estudiante)+1):
        matriz.append([])
        for columna in range(len(materia)):
            matriz[fila].append(0)
def mostrar():
    for i in range(len(matriz)):
        for u in range(len(matriz[0])):
            print(matriz[i][u], end=" ")
        print()
def promedio():
    suma=0
    for i in range(1,len(materia)):
        for j in range(1,len(estudiante[0])):
            suma+=matriz[i][j]
    total_elementos=(len(materia)-1)*(len(estudiante)-1)
    promedio=suma/total_elementos
    print("El promedio es: ", promedio)

crearmatriz()
x = -1
for i in range(len(matriz)):
    for w in range(len(matriz[0])):
        if i == 0:
            matriz[i][w]=materia[w]
        elif x==0:
            matriz[i][w]=estudiante[x]
    x+=1
    for i in range(len(materia)):
        for p in range(1, len(matriz[0])-1):
            matriz[i][p]=random.randint(0,10)
mostrar()
promedio(matriz)