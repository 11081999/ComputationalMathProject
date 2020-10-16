from texttable import Texttable
t = Texttable()
t2 = Texttable()

import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np
np.set_printoptions(suppress=True)

#from graphviz import * as graph
originalFile = "test1.txt"
with open(originalFile) as file_in:
    lines = []
    for line in file_in:
        line = line.rstrip()
        lines.append(line)

#Recoger valores de la primera fila del .txt y ordenarlos en un array (q0, q1, q2, q3)
nodes= lines[0].split(',')
print("\n Nodes: ")
print(nodes)

#Recoger los valroes de la segunda fila del .txt y agregarlos a un array (a,b)
valores= lines[1].split(',')
print("\n Valores: ")
print(valores)

#Declarar la variable del estado inicial
initialState= lines[2]
print("\n Initial State: ")
print(initialState)

#Dclarar los lygares en donde es estado final
finalStates= lines[3].split(',')
print("\n Estados Finales: ")
print(finalStates)

#Make transition table basado en los valores de la quinta linea hasta n
rows, cols = (len(nodes)+1, len(valores)+1)
table = [[0 for i in range(cols)] for j in range(rows)]

for i in range(0, len(valores)+1):
    if i == 0:
        table[0][i]= "QN"
    else:
        table[0][i]= valores[i-1]

def contarNodos(nodo):
    counter= 0
    for i in range(4, len(lines)):
        currentLine = lines[i].split(',')
        currentNode = currentLine[0]
        if currentNode == nodo:
            counter += 1
    return counter

def findLine(node, jumps):
    counter= 1
    for i in range(4, len(lines)):
        currentLine = lines[i].split(',')
        currentNode = currentLine[0]
        if currentNode == node:
            if counter == jumps:
                return currentLine
                break
            counter += 1

    return "null"

def isFinal(node):
    if node in finalStates:
        return True

tableSpot= 1
#nodesBlackList= [0 for i in range(0, len(nodes))]
nodesBlackList= []
for i in range(4, len(lines)):
    currentLine = lines[i].split(',')
    currentNode = currentLine[0]

    if not currentNode in nodesBlackList:
        nodesBlackList.append(currentNode)
        table[tableSpot][0]= currentNode
        for j in range(1, contarNodos(currentNode)+1):
            if findLine(currentNode, j) != "null":

                print(findLine(currentNode, j))
                print(j)

                currentLine= findLine(currentNode, j)
                #Node
                lineNode  = currentLine[0]
                #
                lineValuePointer = currentLine[1]
                #
                value = lineValuePointer[3: len(lineValuePointer)]
                direction= lineValuePointer[0]

                table[tableSpot][table[0].index(direction)] = str(value)

        if tableSpot < len(nodes):
            tableSpot+= 1;

#print("\n BlackList: ")
#print(nodesBlackList)

#print("\n Transition table 1: ")
#print(table)
print("\n Transition table (OG): ")
t.add_rows(table)
print(t.draw())

def minimize(rowOne, i, rowTwo, j):
    rowOneNode= table[0][i]
    rowTwoNode= table[0][j]

    #for a in range(0, len(table)):
        #if

#De la tabla de transicion buscar valores exactamente iguales (por fila) de los nodos y los valores
rowsBlackList= []
for i in range(1, len(table)):
    masterRow=  np.array(table[i][1:len(nodes)])
    for j in range(1, len(table)):
        print("-------j----------------")
        subRow= np.array(table[j][1:len(nodes)])
        if (masterRow==subRow).all() and i != j:
            print("Found Duplicate at row: "+ str(j))

            rowsBlackList.append(j)



print("BL")
print(rowsBlackList)

#print("\n Transition table (MIN): ")
#t2.add_rows(table)
#print(t2.draw())





#Pedir un input, y imprimir si ese imput (string) es aceptado por el DFA

#De la tabla minimizada imprimir el arbol y poder pedir inut y decir si es aceptado por el DFA


"""
step= 4
for i in range(0, len(nodes)):
    currentLine = lines[step].split(',')
    currentNode = currentLine[0]
    table[i][0] = currentNode
    step+= contarNodos(currentNode)

step= 4
for i in range(0, len(nodes)):
    currentLine = lines[step].split(',')
    currentNode   = currentLine[0]
    currentrEntry = currentLine[1]
    stringOne     = currentrEntry[0]
    stringTwo     = currentrEntry[3: len(currentrEntry) - 1]
    table[i][1] = str(stringOne) + ":" + str(stringTwo)
    step += contarNodos(currentNode)

step= 4
for i in range(0, len(nodes)):
    if (step < len(lines)-1):
        currentLine = lines[step+1].split(',')
        currentNode   = currentLine[0]
        currentrEntry = currentLine[1]
        stringOne     = currentrEntry[0]
        stringTwo     = currentrEntry[3: len(currentrEntry) - 1]
        table[i][2] = str(stringOne) + ":" + str(stringTwo)
        step += contarNodos(currentNode)



preveusNode = " "
for i in range(0, 4):
    currentLine   = lines[i + 4].split(',')
    currentNode   = currentLine[0]
    currentrEntry = currentLine[1]
    stringOne     = currentrEntry[0]
    stringTwo     = currentrEntry[3: len(currentrEntry) - 1]

    table[i][0] = currentNode

    for j in range(0, 3):


        #if currentNode != preveusNode:
            #table[i][j] = currentNode
            #table[i][j] = str(stringOne) + ":" + str(stringTwo)

        elif currentNode == preveusNode:
            nextLine = lines[i + 4 + 1].split(',')
            nextEntry = nextLine[1]
            stringOne = nextEntry[0]
            stringTwo = nextEntry[3: len(nextEntry) - 1]
            table[i][j] = str(stringOne) + ":" + str(stringTwo)


    preveusNode= currentNode

"""