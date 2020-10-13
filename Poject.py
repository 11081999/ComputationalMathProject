
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

totalNodes= len(lines[0])/3
print("\n Number of Nodes: " + str(totalNodes))
#nodes= [0 for i in range(0, int(totalNodes))]

nodes= lines[0].split(',')
print("\n Nodes: ")
print(nodes)

#Recoger los valroes de la segunda fila del .txt y agregarlos a un array (a,b)
valores= lines[1].split(',')
print("\n Second line: ")
print(valores)

#Declarar la variable del estado inicial
initialState= lines[2]

#Dclarar los lygares en donde es estado final
#final= []

#Make transition table basado en los valores de la quinta linea hasta n
#transTable= [][]

#De la tabla de transicion buscar valores exactamente iguales (por fila) de los nodos y los valores

#Pedir un input, y imprimir si ese imput (string) es aceptado por el DFA

#De la tabla minimizada imprimir el arbol y poder pedir inut y decir si es aceptado por el DFA