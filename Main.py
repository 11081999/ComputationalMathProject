"""
    Texttable is a library that helps visualize the minimized table
    in a friendly format to the eyes.
"""
from texttable import Texttable
t = Texttable() #t will be the reference to the library texttable


#For some reason sometime Numpy fails to download in pycharm so as an alternative you can highlight the path in you files
#--WARNING!-- If this is NOT the case for you then comment!
import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
"""
    Nunpy is a library that helps to compare and organize arrays in order
    to save procesess. 
"""
import numpy as np
np.set_printoptions(suppress=True)

"""
    Graphiz could help to print in a graphic interface the DFA
"""
#from graphviz import * as graph

"""
    This process opens the designated file and orders every line in an array
"""
originalFile = "test2.txt"
with open(originalFile) as file_in:
    lines = []                      #This array will store every line of the file in thir own index, in order.
    for line in file_in:
        line = line.rstrip()        #Sometimes the end of the line will keep a "\n" so this code removes it because it affects comparisons
        lines.append(line)

"""
    OBJECTIVE:
    Makeaprogram  that  reads  from  a  file the  elements  that  define  an DFAand buildsthe equivalent minimized DFA.
    Also, the program should say if a string is accepted or not by any DFA
"""
"""  
    The following assignations represent the "data gathering" according to the activiy, it goes as follows:
    -The first lineindicatesthe set of states of the automataseparatedby commas.
    -The second line indicates the alphabet symbols separated by commas
    -The third line indicates the initial state
    -The fourth line indicates the set of final states separated by commas.
    
    -Thefollowing  lines  indicate  the  evaluation  of  the  extended  transition  function  with  
    the elements of the alphabetin the following format:
    
    state,symbol = > state
    
    Eg. q0, a = > q1
    
"""
#This variable stores the values on the first line of the .txt file, these are the nodes
nodes= lines[0].split(',') #--Observation-- the .split() function return an array with every index being what was beside the parameter
print("\n Nodes: ")
print(nodes)

#This variable stores the values on the second line of the .txt file, these are the possbile values a node can evaluate
valores= lines[1].split(',')
print("\n Valores: ")
print(valores)

#This variable stores the values on the third line of the .txt file, these are the possbile initial states
initialState= lines[2]
print("\n Initial State: ")
print(initialState)

#This variable stores the values on the third line of the .txt file, these are the final states
finalStates= lines[3].split(',')
print("\n Estados Finales: ")
print(finalStates)

"""
    The following proceses will take on the task of building the transition table based on the data gathered and
    The instructions of this activity. For this well purely muse array manipulation although an alternative would be
    to use dicctionaries. The porblem was tackled with 1D and 2D arrays because even if we use dicctionaries a table
    must be built up in order to minimize and evaluate atrings.
"""

#Dinamically fill 2D array wich will be the transition
rows, cols = (len(nodes)+1, len(valores)+1)
table = [[0 for i in range(cols)] for j in range(rows)]

"""
    This process Dinamically fills the top row of the transition table
"""
for i in range(0, len(valores)+1):
    if i == 0:
        table[0][i]= "QN"
    else:
        table[0][i]= valores[i-1]

"""
    This function recieves a node in order to determine how many nodes of the same type are in the text file
    This serves in the second loop in order for it to repeat as many times as the nodes repeat int the .txt file,
    this makes for an autonomus way to look for information on the same node and store it on the table
"""
def contarNodos(nodo):
    counter= 0
    for i in range(4, len(lines)):
        currentLine = lines[i].split(',')
        currentNode = currentLine[0]
        if currentNode == nodo:
            counter += 1
    return counter

"""
    This function recieves a node and a jump, the jump referes to the iteration on the loop it is called from and this value
    represents the number of times the same node has been found in the .txt file. For example if whe have q0 pointing to a on
    one line and on the next one q0 poitning to b then if we already catalogued q0 goes to a in our transition table then
    the program "jumps" to the next q0. If we have already worked with all the nodes of one type in all lines we return "null"
    
    --Observation-- The "jumps" is the j value on the second loop when filling the table, this value is also the result given by contarNodos()
    
"""
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


"""
    This function checks if the given node is final. This need to be taken into consideration when trying to merge rows
    at the step of minimization

"""
def isFinal(node):
    if node in finalStates:
        return True

"""
    The following proceses will at last build the transition table. The way of doing this is by keeping track on the row
    of the table we are in -tableSpot- and also keeping track of the nodes we have already filled, if we have then add
    them to the -nodesBlackList-. The nodes and values to add in the table are taken directly from the array of -lines-
    it mjust be notet that the scann of the prccess starts at line 4 and ends an the end of the array of -lines-.
    
    On the first loop the task is to iterate each line and get the node in question, if the node has not been already 
    worked with then we add it to the blacklist and move on to the second loop
    
    On the second loop  
    
"""
tableSpot= 1         #--Observation-- tableSpot starts at 1 because the first row and column are to display te main nodes and values
nodesBlackList= []
for i in range(4, len(lines)):
    currentLine = lines[i].split(',')
    currentNode = currentLine[0]

    if not currentNode in nodesBlackList:
        nodesBlackList.append(currentNode)
        table[tableSpot][0]= currentNode
        for j in range(1, contarNodos(currentNode)+1):
            if findLine(currentNode, j) != "null":

                #print(findLine(currentNode, j))
                #print(j)

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
print("\n Transition table (ORIGINAL): ")
print(table)

#De la tabla de transicion buscar valores exactamente iguales (por fila) de los nodos y los valores
def findDuplicateRowsOnTable():
    rowsBlackList= []
    for i in range(1, len(table)):
        masterRow=  np.array(table[i][1:len(nodes)])
        for j in range(1, len(table)):
            subRow= np.array(table[j][1:len(nodes)])
            if (masterRow==subRow).all() and i != j:

                print("Found Duplicate at row: "+ str(j))
                rowsBlackList.append(j)
    return rowsBlackList
    print("BL")
    print(rowsBlackList)

def getRowsSameTye(row):
    messsage = "Duplicate of row "+str(row)
    masterRow=  np.array(table[row][1:len(nodes)])
    rowtypes= []
    rowtypes.append(row)
    for i in range(1, len(table)):
        subRow= np.array(table[i][1:len(nodes)])

        #Take into consideration final states & also change final states
        if (masterRow==subRow).all() and row != i:
            messsage+= " at "+str(i)
            rowtypes.append(i)
    print(messsage)
    return rowtypes



def minimize():
    print("-------------------------")
    duplicateRows = findDuplicateRowsOnTable()

    if not len(duplicateRows) <= 0:
        print("Duplicate Rows:")
        print(duplicateRows)
        rowType = getRowsSameTye(duplicateRows[0])
        print("Duplicate Rows Same Type:")
        print(rowType)

        minimizationSymbol = str(table[duplicateRows[0]][0]) + "M"
        print("Symbol:")
        print(minimizationSymbol)

        targetToReplace = []
        targetToReplace.append(table[rowType[0]][0])
        targetToReplace.append(table[rowType[1]][0])
        print("Replace:")
        print(targetToReplace)

        for i in range(1, len(rowType)):
            #Should be careful no to delete any initial states
            del table[rowType[i]]

        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                for z in range(0, len(targetToReplace)):
                    if table[i][j] == targetToReplace[z]:
                        table[i][j] = minimizationSymbol


minimize()
minimize()

print("\n Transition table (MINIMIZED): ")
t.add_rows(table)
print(t.draw())

#def testCharDFA(start):


def testStringInDFA(start, string, char):
    if(len(string) == char):
        if start in finalStates:
            return print("The string belong in the DFA")
        else:
            return print("The string des not belong in the DFA")

    columnNodes=[]
    for i in range(1, len(table)):
        columnNodes.append(table[i][0])

    print("-------------------------")
    #startNode
    print("Current Node: ")
    print(str(start))
    nodeBranches= table[(columnNodes).index(start)+1][1:len(nodes)]
    print("Node Branches: ")
    print(nodeBranches)

    stringPath= ""
    charPos= valores.index(string[char])
    nextNode= nodeBranches[charPos]
    stringPath += "process " + str(string[char]) + " Goes to " + str(nextNode)
    print(stringPath)

    testStringInDFA(nextNode, string, char+1)

    #for ch in range(0, len(string)):
        #if start in table[i+1][1:len(nodes)]:




print("Introcude a tring to evaluate")
#inputString= str(input())
inputString= "abab"
testStringInDFA(initialState, inputString, 0)







