from generateTree import GenerateFamilyTree
from inputTaskFunctions import InputTaskFunction

if __name__ == '__main__':
    familyTree = GenerateFamilyTree()
    listOfFamilyTreeNode = familyTree.create_member_nodes()
    familyTree.add_child_to_mother(listOfFamilyTreeNode)
    familyHead = listOfFamilyTreeNode[0]
    inputFile = open('inputData.txt', 'r+')
    task = InputTaskFunction()

    # inputFile = open(sys.argv[1], 'r+')
    # -------- Below block adds_child and gets_relation ------- #
    for eachLine in inputFile.readlines():
        inputTask = eachLine.split(' ')[0]
        if inputTask == 'ADD_CHILD' :
            motherName = eachLine.split(' ')[1]
            childName = eachLine.split(' ')[2]
            childGender = eachLine.split(' ')[3]
            task.add_input_child(motherName,childName,childGender, familyHead)
        elif inputTask == 'GET_RELATIONSHIP':
            memberName = eachLine.split(' ')[1]
            relation = eachLine.split(' ')[2].replace('\n','')
            task.get_relationship(memberName, relation, familyHead)
        else:
            print('No Such Task Defined in The Problem Statement')

    inputFile.close()
