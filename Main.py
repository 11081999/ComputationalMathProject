"""
    IMPORTANT__ in order to run program

    import texttable
    import numpy

    ! test file should be addressed at line 36

    ! TRANSITION TABLE at line 172

    ! MINIMIZATION at line at 254

    ! VALIDATE STRING at 303

    ! Input to validate in DFA should always remain a string without spaces

"""
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
#--Observation-- values must be remembered as where the node is pointing to
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
    
    On the second loop we get the line of the node we are working with and assing the values it had on that line, we then
    look for other lines with information on the same node in order to determine if it has more values. 
    All the valid values will be stored in order. 
    
    --Observation-- On the second iteration we assume the arr -values- are in order as well as the values readed by findLine()
                    and are coincidentally the same based on the given format for test.2 and test.1
    
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
                #Values of the node (where the node is pointing to)
                lineValuePointer = currentLine[1]


                # --Observation-- at this point the string of value is still in the form of "b=>q6"
                value = lineValuePointer[3: len(lineValuePointer)] #the index here refers to the substring from the position 3 to the end of the same string.
                direction= lineValuePointer[0]

                # Dinamically save the value on the next spot -tableSpot-
                table[tableSpot][table[0].index(direction)] = str(value)

        if tableSpot < len(nodes):
            tableSpot+= 1;

#print("\n BlackList: ")
#print(nodesBlackList)
#print("\n Transition table (ORIGINAL): ")
#print(table)

"""
    This function looks for duplicate rows on the the transition table, it returns every row that is duplicate even if the pairs are different between eachother
"""
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

"""
    This function unlike the latter, looks for duplicate rows of the same type. And returns the repeated rows except the
    first one that was found. The remaining will later be erased from the table.
"""
def getRowsSameTye(row):
    messsage = "Duplicate of row "+str(row)
    masterRow=  np.array(table[row][1:len(nodes)])
    rowtypes= []
    rowtypes.append(row)
    for i in range(1, len(table)):
        subRow= np.array(table[i][1:len(nodes)])

        #--WARNING!--   Take into consideration final states & also change final states
        #               Wich currently are not taken into consideration
        if (masterRow==subRow).all() and row != i:
            messsage+= " at "+str(i)
            rowtypes.append(i)
    print(messsage)
    return rowtypes

"""
    This function will minimize the transition table only once, in case of having more roes it should be called again
    The function determines the duplicate rows, and then determines of those witch ones are the same.
    Then, it determines a new symbol to replace the duplicated rows and also calculates the nodes it needs to replace;
    this is so we can delete one of the duplicated rows. 
    for this, it loops though the whole table and replaces the old nodes for the new ones. 
    Always, the values it will replace in the table will be the node on the first column
"""
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

        #The idea here is to automatically assign values, but works for the scope of a,b
        targetToReplace = []
        targetToReplace.append(table[rowType[0]][0])
        targetToReplace.append(table[rowType[1]][0])
        print("Replace:")
        print(targetToReplace)

        for i in range(1, len(rowType)):
            #--WARNING!-- Should be careful no to delete any initial states
            del table[rowType[i]]

        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                for z in range(0, len(targetToReplace)):
                    if table[i][j] == targetToReplace[z]:
                        table[i][j] = minimizationSymbol


#We hardcode call minimze twice but in reality it shiuld be auromated to call every time it detects anoder duplicate row
minimize()
minimize()

print("\n Transition table (MINIMIZED): ")
t.add_rows(table)
print(t.draw())

"""
    This function will test via a recursion if a string belongs to a DFA. In recieves a node to start from, the string
    to evaluate and a number wich wil represent the current position of the string.
    The recursion will then take the next node of the current tecursion as the strating node of th enext recursion. The
    next node is determied by consulting the minimized DFA. 
    The recursion wil end if the char reaches the length of the string, menaing that we have analized every character.
    Or if we are still analyzing and we reach a node without a value then exit immediatly.  
"""
def testStringInDFA(start, string, char):
    if(len(string) == char):
        if start in finalStates:
            return print("\n The string belong in the DFA")
        else:
            return print("\n The string des not belong in the DFA")

    if start == 0:
        return print("\n The string des not belong in the DFA")

    columnNodes=[]
    for i in range(1, len(table)):
        columnNodes.append(table[i][0])

    print("-------------------------")
    #startNode
    print("Current Node: ")
    print(start)
    nodeBranches= table[(columnNodes).index(start)+1][1:len(nodes)]
    print("Node Branches: ")
    print(nodeBranches)

    stringPath= ""
    charPos= valores.index(string[char])
    nextNode= nodeBranches[charPos]
    stringPath += "process " + str(string[char]) + " Goes to " + str(nextNode)
    print(stringPath)

    testStringInDFA(nextNode, string, char+1)


"""
    Se espera que cualquier lector competente del tema pueda descomentar el inputString y comentar el que recive un input
    par aprovar la funcianalidad del metodo testStringInDFA()
"""
print("Introcude a string to evaluate")
##Ask for input as a string
inputString= str(input())
#inputString= "abab"
#Evaluate Strinf Input
testStringInDFA(str(initialState), inputString, 0)







