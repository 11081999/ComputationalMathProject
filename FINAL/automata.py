import collections
from node import Node
import sys
import copy


class AUTOMATA:
    def __init__(self):
        self.nodes = collections.OrderedDict()
        self.symbols = []
        self.first = None

    def getNodes(self):
        return self.nodes

    def getFirst(self):
        return self.first

    def addNode(self, node):

        self.nodes[node.getName()] = node

        if self.first is None:
            self.first = node.getName()

        self.updateSymbols()


    def updateSymbols(self):
        for nodeName, node in self.nodes.items():

            for symbol, transition in node.getTransitions().items():

                if (not symbol in self.symbols) and symbol != "E":
                    self.symbols.append(symbol)

                    self.symbols.sort()

    def isAFD(self):

        for nodeName, node in self.nodes.items():

            transitions = node.getTransitions()

            if len(transitions) < len(self.symbols):
                return False


            for symbol, destinations in transitions.items():

                if len(str(symbol)) > 1:
                    return False

                if len(destinations) > 1:
                    return False

        return True


    def minimize(self):

        if self.isAFD():

            groups = {}
            groupByName = {}


            for nodeName, node in self.nodes.items():

                groupID = 1

                if node.isFinal():
                    groupID = 2

                if not groupID in groups:
                    groups[groupID] = []

                groups[groupID].append(node)
                groupByName[node.getName()] = groupID

            self._minimize(groups, groupByName)
        else:
            print ("No se puede minimizar un AFND, para esto debe ejecutar %s afd %s %s minimo" % (sys.argv[0], sys.argv[2], sys.argv[3]))
            sys.exit()

    def _minimize(self, groups, groupByName):
        nextGroupID = 1

        newGroups = {}
        newGroupByName = {}

        for gID, group in groups.items():

            groupByTransitions = {}

            for node in group:

                transitions = node.getTransitions()

                sortedTransitions = []
                transitionGroups = []

                for symbol in self.symbols:

                    sortedTransitions.append(transitions[symbol][0])

                for transition in sortedTransitions:
                    transitionGroups.append(groupByName[transition])

                transitionString = '|'.join(str(v) for v in transitionGroups)

                if transitionString in groupByTransitions:
                    groupID = groupByTransitions[transitionString]
                else:

                    groupID = nextGroupID
                    groupByTransitions[transitionString] = groupID
                    newGroups[groupID] = []

                    nextGroupID += 1

                newGroups[groupID].append(node)
                newGroupByName[node.getName()] = groupID

        if groups == newGroups:
            self._deleteDuplicates(newGroups)
        else:

            self._minimize(newGroups, newGroupByName)

    def _deleteDuplicates(self, groups):

        for groupId, group in groups.items():

            if len(group) > 1:
                validNode = None

                for duplicatedNode in group:

                    if validNode is None:
                        validNode = duplicatedNode
                    else:

                        del self.nodes[duplicatedNode.getName()]

                        for nodeName, node in self.nodes.items():
                            node.replaceTransition(validNode.getName(), duplicatedNode.getName())


    def __repr__(self):
        return "<AF symbols: '%s', nodes: '\n%s'>" % (self.symbols, self.nodes)
