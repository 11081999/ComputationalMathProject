from automata import AUTOMATA
from node import Node
import sys
import os.path
import copy
import linecache


class MAIN:
    def __init__(self):

        args = sys.argv

        validActions = ["minimizar"]

        if (len(args) < 2) or (args[1] not in validActions):
            print("Accion no valida")
            sys.exit()

        action = args[1]

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
        #line4[0] = "Final"
       # f = open(filename)

        with open(filename) as f:
            for i in range(4):
                f, next(f)
            for line in f:

                line = line.rstrip()
                print(line)

                data = line.split()
                print(data)

                if len(data) > 1:

                    nodeName = data[0]


                    final = True if data[0] in line4 else False
                    print(final)

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