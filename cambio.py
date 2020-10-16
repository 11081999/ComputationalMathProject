originalFile = "Test1.txt"
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

rows= len(nodes)
formatoDelMin = [0 for i in range(rows)]

def contarNodos(nodo):
    counter= 0
    for i in range(4 , len(lines)):
        currentLine = lines[i].split(',')
        currentNode = currentLine[0]
        if currentNode == nodo:
            counter += 1
    return counter

step= 4
for i in range(0, len(nodes)):
    if any(nodes[i] in s for s in finalStates):
        formatoDelMin[i] = str(nodes[i]).upper() + " FINAL"
    else:
        formatoDelMin[i] = str(nodes[i]).upper() + " NOFINAL"

    print("\n J: ")
    ##Por alguna razon la ultima entrada tiene \ln y eso puede perjudicar a la hora de comparar elementos
    for j in range(0, contarNodos(nodes[i][0: 2])):
        currentLine = lines[step+j].split(',')

        print(currentLine)
        currentrEntry = currentLine[1]
        stringOne = currentrEntry[0]
        stringTwo = currentrEntry[3: len(currentrEntry)]
        formatoDelMin[i] += " " + str(stringOne).upper() + "=>" + str(stringTwo)

    step += contarNodos(nodes[i])

formatDocuemtnText = ["", "", "", ""]
formatDocuemtnText.extend(formatoDelMin)

print("\n Estados del Min Doc: ")
print(formatDocuemtnText)

formatDocument = open("SecondCode/format.txt", "a")
formatDocument.writelines("%s\n" % l for l in formatDocuemtnText)
formatDocument.close()
