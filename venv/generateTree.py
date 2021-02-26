from familyTree import FamilyTreeNode

class GenerateFamilyTree:

    def add_single_member(self,memberData):
        memberName = memberData[0]
        memberGender = memberData[1].replace('\n', '')
        node = FamilyTreeNode(memberName, memberGender)
        return node

    def add_member_with_partner(self, memberData):
        memberName = memberData[0]
        memberGender = memberData[1]
        memberSpouseName = memberData[2]
        memberSpouseGender = memberData[3].replace('\n', '')
        node = FamilyTreeNode(memberName, memberGender, memberSpouseName, memberSpouseGender)
        return node


    def create_member_nodes(self):
        familyMemberFile = open('familyMember.txt', 'r+')
        listOfFamilyMemberNode = []
        for eachLine in familyMemberFile:
            memberData = eachLine.split(' ')
            if len(memberData) == 2:
                treeNode = self.add_single_member(memberData)
                listOfFamilyMemberNode.append(treeNode)
            else:
                treeNode = self.add_member_with_partner(memberData)
                listOfFamilyMemberNode.append(treeNode)
        familyMemberFile.close()

        return listOfFamilyMemberNode

    def search_parent_in_listOfFamilyMemberNode(self, motherName, listOfFamilyMemberNode):
        parentNode = None
        for member in listOfFamilyMemberNode:
            if member.if_member_is_married() :
                if member.name == motherName or member.spouseName == motherName:
                    parentNode = member
        if parentNode is None:
            print("PERSON_NOT_FOUND")
        else:
            return parentNode

    def search_child_in_listOfFamilyMemberNode(self, childName, listOfFamilyMemberNode):
        childNode = None
        for member in listOfFamilyMemberNode:
            if member.name == childName :
                childNode = member

        if childNode is None:
            raise TypeError("Child Not Found")
        else:
            return childNode


    def add_child_to_mother(self, listOfFamilyMemberNode):
        memberRelationFile = open('familyMemberRelation.txt', 'r+')
        for eachLine in memberRelationFile:
            motherName = eachLine.split(' ')[0]
            childName = eachLine.split(' ')[1].replace('\n','')
            parentNode = self.search_parent_in_listOfFamilyMemberNode(motherName, listOfFamilyMemberNode)
            childNode = self.search_child_in_listOfFamilyMemberNode(childName, listOfFamilyMemberNode)
            parentNode.add_child_node(childNode)
        memberRelationFile.close()
