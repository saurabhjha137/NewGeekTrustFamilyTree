from familyTree import FamilyTreeNode
from getRelationships import GetRelationship


class InputTaskFunction:
    # searches the member in the Family tree using rootNode
    # i.e. familyHead which is KingShan
    def search_member_using_familyHead(self, familyHead, memberName):
        if familyHead.name == memberName or familyHead.spouseName == memberName:
            return familyHead
        else:
            for child in familyHead.children:
                testChild = self.search_member_using_familyHead(child, memberName)
                if testChild:
                    return testChild

    # adds child to Family tree
    def add_child_to_familyTree(self, parent, motherName, childName, childGender):
        if parent.is_mother(motherName):
            newMember = FamilyTreeNode(childName, childGender)
            parent.add_child_node(newMember)
            print("CHILD_ADDITION_SUCCEEDED")
        else:
            print("CHILD_ADDITION_FAILED")

    # if parent is found adds child to Family Tree
    def add_input_child(self, motherName, childName, childGender, familyHead):
        parent = self.search_member_using_familyHead(familyHead, motherName)
        if parent:
            self.add_child_to_familyTree(parent, motherName, childName, childGender)
        else:
            print("PERSON_NOT_FOUND")

    # based on relation value finds relatives of the given member
    # uses GetRelationShip class to find relation

    def get_relationship(self, memberName, relation, familyHead):
        member = self.search_member_using_familyHead(familyHead, memberName)
        relative = GetRelationship(member)
        if member:
            if relation == "Son":
                listOfRelatives = relative.get_sons()
            elif relation == "Daughter":
                listOfRelatives = relative.get_daughters()
            elif relation == "Siblings":
                listOfRelatives = relative.get_siblings()
            elif relation == "Paternal-Uncle":
                listOfRelatives = relative.get_paternal_uncle()
            elif relation == "Paternal-Aunt":
                listOfRelatives = relative.get_paternal_aunty()
            elif relation == "Maternal-Uncle":
                listOfRelatives = relative.get_maternal_uncle()
            elif relation == "Maternal-Aunt":
                listOfRelatives = relative.get_maternal_aunty()
            elif relation == "Brother-In-Law":
                listOfRelatives = relative.get_brother_in_law(memberName)
            elif relation == "Sister-In-Law":
                listOfRelatives = relative.get_sister_in_law(memberName)
            else:
                listOfRelatives = []
            if listOfRelatives != []:
                #print(listOfRelatives)
                print(" ".join(listOfRelatives))
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")
