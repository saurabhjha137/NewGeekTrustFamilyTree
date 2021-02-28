from generateTree import GenerateFamilyTree
from inputTaskFunctions import InputTaskFunction

class InputOutputTask:
    # adds input child in the FamilyTree
    def adding_child(self, eachLine, familyHead):
        task = InputTaskFunction()
        motherName = eachLine.split(' ')[1]
        childName = eachLine.split(' ')[2]
        childGender = eachLine.split(' ')[3].replace('\n', '')
        task.add_input_child(motherName, childName, childGender, familyHead)

    # find relative for the given member
    def geting_relationship(self, eachLine, familyHead):
        task = InputTaskFunction()
        memberName = eachLine.split(' ')[1]
        relation = eachLine.split(' ')[2].replace('\n', '')
        task.get_relationship(memberName, relation, familyHead)

    # performs task given in the input
    # i.e. ADD_CHILD and GET_RELATIONSHIP
    def perform_input_task(self, inputFile):
        for eachLine in inputFile.readlines():
            inputTask = eachLine.split(' ')[0]
            if inputTask == 'ADD_CHILD':
                self.adding_child(eachLine,familyHead)
            elif inputTask == 'GET_RELATIONSHIP':
                self.geting_relationship(eachLine,familyHead)
            else:
                print('No Such Task Defined in The Problem Statement')


if __name__ == '__main__':
    # generating initial FamilyTree
    familyTree = GenerateFamilyTree()
    listOfFamilyTreeNode = familyTree.create_member_nodes()
    familyTree.connect_child_to_mother(listOfFamilyTreeNode)
    familyHead = listOfFamilyTreeNode[0]

    # -------- Below block adds_child and gets_relation ------- #
    inputOutput = InputOutputTask()
    inputFile = open('inputData.txt', 'r+')
    # inputFile = open(sys.argv[1], 'r+')
    inputOutput.perform_input_task(inputFile)

    inputFile.close()
