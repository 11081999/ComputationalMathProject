from automata import AUTOMATA
from node import Node
import sys
import os.path
import copy
import linecache

#python main.py minimizar Prueba.txt Resultados6.txt

##


class MAIN:
    def __init__(self):

        args = sys.argv

        validActions = ["minimizar"]

        if (len(args) < 2) or (args[1] not in validActions):
            print("Accion no valida")
            sys.exit()

        action = args[1]

        originalFile = args[2]
        with open(originalFile) as file_in:
            lines = []
            for line in file_in:
                line = line.rstrip()
                lines.append(line)

        # Recoger valores de la primera fila del .txt y ordenarlos en un array (q0, q1, q2, q3)
        nodes = lines[0].split(',')
        print("\n Nodes: ")
        print(nodes)

        # Recoger los valroes de la segunda fila del .txt y agregarlos a un array (a,b)
        valores = lines[1].split(',')
        print("\n Valores: ")
        print(valores)

        # Declarar la variable del estado inicial
        initialState = lines[2]
        print("\n Initial State: ")
        print(initialState)

        # Dclarar los lygares en donde es estado final
        finalStates = lines[3].split(',')
        print("\n Estados Finales: ")
        print(finalStates)

        rows = len(nodes)
        formatoDelMin = [0 for i in range(rows)]

        def contarNodos(nodo):
            counter = 0
            for i in range(4, len(lines)):
                currentLine = lines[i].split(',')
                currentNode = currentLine[0]
                if currentNode == nodo:
                    counter += 1
            return counter

        step = 4
        for i in range(0, len(nodes)):
            if any(nodes[i] in s for s in finalStates):
                formatoDelMin[i] = str(nodes[i]).upper() + " FINAL"
            else:
                formatoDelMin[i] = str(nodes[i]).upper() + " NOFINAL"

            print("\n J: ")
            ##Por alguna razon la ultima entrada tiene \ln y eso puede perjudicar a la hora de comparar elementos
            for j in range(0, contarNodos(nodes[i][0: 2])):
                currentLine = lines[step + j].split(',')

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

        formatDocument = open("format.txt", "a")
        formatDocument.writelines("%s\n" % l for l in formatDocuemtnText)
        formatDocument.close()

        if action == "minimizar":
            return self._minimizar(args)

    def _loadFromFile(self, automata, filename):
        if not os.path.isfile(filename):
            print("El archivo indicado no existe.")
            sys.exit()

        line4 = linecache.getline(filename, 4)
        line4 = line4.rstrip()
        print(line4)
        line4 = line4.split(",")
        print(line4)
        line4[0] = "Final"
        f = open(filename)

        with open(filename) as f:
            for i in range(4):
                f, next(f)
            for line in f:

                line = line.rstrip()

                data = line.split()

                if len(data) > 1:

                    nodeName = data[0]


                    final = True if data[1] == 'FINAL' else False

                    node = Node(nodeName, final)

                    del data[:1]

                    for transition in data:

                        transition = transition.split("=>")
                        if len(transition) == 2:

                            node.addTransition(transition[0], transition[1])

                    automata.addNode(node)

    def _writeOnFile(self, automata, filename):
        f = open(filename, "w")

        for nodeName, node in automata.getNodes().items():

            line = "%s %s" % (node.getName(), "FINAL" if node.isFinal() else "NOFINAL")

            for symbol, transition in node.getTransitions().items():
                for destinationNode in transition:
                    line += " %s=>%s" % (symbol, destinationNode)

            line += "\n"
            f.write(line)

        f.close()


    def _minimizar(self, args):

        if (len(args) < 4):
            print("El uso del programa debe ser: %s %s <archivo de datos> <archivo de resultado>") % (
                args[0], args[1])
            sys.exit()

        dataFile = args[2]
        resultFile = args[3]

        automata = AUTOMATA()

        self._loadFromFile(automata, dataFile)

        automata.minimize()

        self._writeOnFile(automata, resultFile)

        print("Automata minimizado en: %s" % (resultFile))

MAIN()