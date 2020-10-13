
#from graphviz import * as graph
with open("test1.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)



#https://stackoverrun.com/es/q/3344316


#Arrays
#Array= []
#set1.append(set[i])s

#Strings
#String[1]
#len(string)
#string.find()


#Recoger valores de la primera fila del .txt y ordenarlos en un array (q0, q1, q2, q3)

#totalNodes= len(lines[0])/3
#print("\n Number of Nodes: " + str(totalNodes))
#nodes= [0 for i in range(0, int(totalNodes))]

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

rows, cols = (len(nodes), 3)
table = [[0 for i in range(cols)] for j in range(rows)]

textLenght= len(lines)

#len(lines)+1
#0 a 11 - 4

def contarNodos(nodo):
    counter= 0
    for i in range(4 , len(lines)):
        currentLine = lines[i].split(',')
        currentNode = currentLine[0]
        if currentNode == nodo:
            counter += 1
    return counter

print(contarNodos("q3"))

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
"""
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


print(table)






#De la tabla de transicion buscar valores exactamente iguales (por fila) de los nodos y los valores

#Pedir un input, y imprimir si ese imput (string) es aceptado por el DFA

#De la tabla minimizada imprimir el arbol y poder pedir inut y decir si es aceptado por el DFA