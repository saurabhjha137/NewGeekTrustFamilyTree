# single member contains 2 data: name, gender
SINGLE_MEMBER = 2
from familyTree import FamilyTreeNode


class GenerateFamilyTree:
    # creates and return single member node
    def create_single_member(self, memberData):
        memberName = memberData[0]
        memberGender = memberData[1].replace('\n', '')
        node = FamilyTreeNode(memberName, memberGender)
        return node

    # creates and return married member node
    def create_married_member(self, memberData):
        memberName = memberData[0]
        memberGender = memberData[1]
        memberSpouseName = memberData[2]
        memberSpouseGender = memberData[3].replace('\n', '')
        node = FamilyTreeNode(memberName, memberGender, memberSpouseName, memberSpouseGender)
        return node

    # return single or married node
    def single_or_married(self, memberData):
        if len(memberData) == SINGLE_MEMBER:
            createdNode = self.create_single_member(memberData)
        else:
            createdNode = self.create_married_member(memberData)

        return createdNode

    # based on data in file: familyMember.txt
    # create a list of nodes to be added in Family tree
    def create_member_nodes(self):
        familyMemberFile = open('familyMember.txt', 'r+')
        listOfFamilyMemberNode = []
        for eachLine in familyMemberFile:
            memberData = eachLine.split(' ')
            treeNode = self.single_or_married(memberData)
            listOfFamilyMemberNode.append(treeNode)

        familyMemberFile.close()
        return listOfFamilyMemberNode


    # check if name is same or not
    def is_name_same(self, motherName, member):
        return (member.name == motherName) or (member.spouseName == motherName)

    # search parent in the list of created nodes
    # they have to be married
    # their must contain member with motheName
    def search_parent_in_listOfFamilyMemberNode(self, motherName, listOfFamilyMemberNode):
        parentNode = None
        for member in listOfFamilyMemberNode:
            if member.is_married():
                if self.is_name_same(motherName,member) :
                    parentNode = member
        if parentNode is None:
            print("PERSON_NOT_FOUND")
        else:
            return parentNode

    # search child in list of created nodes
    # must have same name as of childName
    def search_child_in_listOfFamilyMemberNode(self, childName, listOfFamilyMemberNode):
        childNode = None
        for member in listOfFamilyMemberNode:
            if member.name == childName:
                childNode = member

        if childNode is None:
            print("No Such Child Node")
        else:
            return childNode

    # based on data in file: familyMemberRelation.txt
    # connects child to their parent node
    def connect_child_to_mother(self, listOfFamilyMemberNode):
        memberRelationFile = open('familyMemberRelation.txt', 'r+')
        for eachLine in memberRelationFile:
            motherName = eachLine.split(' ')[0]
            childName = eachLine.split(' ')[1].replace('\n', '')
            parentNode = self.search_parent_in_listOfFamilyMemberNode(motherName, listOfFamilyMemberNode)
            childNode = self.search_child_in_listOfFamilyMemberNode(childName, listOfFamilyMemberNode)
            parentNode.add_child_node(childNode)
        memberRelationFile.close()
