class FindRelative:
    """
    initializes member with the value of memberNode
    memberNode is reutrned after searching in family tree
    using search_member_using_familyHead in class GenerateFamilyTree
    """
    def __init__(self, memberNode):
        self.member = memberNode

    # comapres if gender is same of both node and member
    def is_name_gender_same(self, node , gender):
        return node.name != self.member.name and node.gender == gender

    # returns list of childNodes after comparison
    # compares gender and name from is_name_gender_same()
    def create_relative_node_list(self, searchNode, gender):
        createdlist = []
        for child in searchNode.children:
            if self.is_name_gender_same(child,gender):
                createdlist.append(child)

        return createdlist

    # returns a list of names of relative, from createdList
    # createdList is returned from create_relative_node_list()
    def add_relative_names(self, createdList):
        relativeName = []
        for memmber in createdList:
            relativeName.append(memmber.name)

        return relativeName

    # finds sibling (brother or sister)
    # for brother siblingGender = 'Male'
    # for sister siblingGender = 'Female'
    def find_sibling(self, siblingGender):
        parent = self.member.parent
        if parent:
            siblingNodeList = self.create_relative_node_list(parent,siblingGender)

        return self.add_relative_names(siblingNodeList)

    # finds (uncle or aunty) (Maternal or Paternal)
    # for PaternalUncle maternalORpaternal = 'Male' and uncleORaunty = 'Male'
    # for MaternalUncle maternalORpaternal = 'Female' and uncleORaunty = 'Male'
    # for PaternalAunty maternalORpaternal = 'Male' and uncleORaunty = 'Female'
    # for MaternalAunty maternalORpaternal = 'Female' and uncleORaunty='Female'
    def find_uncle_aunty(self, maternalORpaternal, uncleORaunty):
        parent = self.member.parent
        grandParent = parent.parent
        if parent.gender == maternalORpaternal:
            uncleAuntyNodeList = self.create_relative_node_list(grandParent,uncleORaunty)

        return self.add_relative_names(uncleAuntyNodeList)

    # In order to find InLaws, one has to find siblings of the member
    # and spouseOfSibling of the member
    # Below function returns list of name of spouseOfSibling
    # if member in the spouseSiblingNodeList is married then
    # their names(name of spouse of member in spouseSiblingNodeList)
    # are appended in spouseOfSibling
    def spouse_of_sibling(self, parent, wifeORhusband):
        spouseSiblingNodeList = self.create_relative_node_list(parent, wifeORhusband)
        spouseOfSibling = []
        for member in spouseSiblingNodeList:
            if member.is_married():
                spouseOfSibling.append(member.spouseName)

        return spouseOfSibling

    # finds (brother-in-law or sister-in-law)
    # for brother-in-law inLawsGender = 'Male' & wifeORhusband = 'Female'
    # brother-in-law ---> Spouse’s brothers, Husbands of siblings
    # for sister-in-Law inLawsGender = 'Female' & wifeORhusband = 'Male'
    # sister-in-Law ---> Spouse’s sisters, Wives of siblings
    def find_in_laws(self, name, inLawsGender, wifeORhusband):
        sibling = []
        spouseOfSibling = []
        parent = self.member.parent

        if self.member.spouseName == name:
            sibling = self.find_sibling(inLawsGender)
        else:
            spouseOfSibling = self.spouse_of_sibling(parent,wifeORhusband)

        return (sibling + spouseOfSibling)
