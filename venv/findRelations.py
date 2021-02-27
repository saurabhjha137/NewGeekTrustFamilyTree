class FindRelationship:
    """"
    initializes member with the value of memberNode
    memberNode is reutrned after searching in family tree
    using search_member_using_familyHead in class GenerateFamilyTree
    """
    def __init__(self, memberNode):
        self.member = memberNode

    # finds children son or daughter
    # for son childGender = 'Male'
    # for daughter childGender = 'Female'
    def find_children(self, childGender):
        children = []
        for child in self.member.children:
            if child.gender == childGender:
                children.append(child.name)

        return children

    # finds sibling (brother or sister)
    # for brother siblingGender = 'Male'
    # for sister siblingGender = 'Female'
    def find_siblings(self, siblingGender):
        siblings = []
        currParent = self.member.parent
        if currParent:
            for child in currParent.children:
                if (child.name is not self.member.name) and \
                        (child.gender == siblingGender):
                    siblings.append(child.name)

        return siblings

    # finds (uncle or aunty) (Maternal or Paternal)
    # for PaternalUncle maternalORpaternal = 'Male' and uncleORaunty = 'Male'
    # for MaternalUncle maternalORpaternal = 'Female' and uncleORaunty = 'Male'
    # for PaternalAunty maternalORpaternal = 'Male' and uncleORaunty = 'Female'
    # for MaternalAunty maternalORpaternal = 'Female' and uncleORaunty='Female'
    def find_uncle_aunty(self, maternalORpaternal, uncleORaunty):
        uncleAunty = []
        currParent = self.member.parent
        suprParent = currParent.parent

        if currParent.gender == maternalORpaternal:
            for child in suprParent.children:
                if (child.gender == uncleORaunty) and \
                        (child.name != currParent.name):
                    uncleAunty.append(child.name)

        return uncleAunty

    # finds (brother-in-law or sister-in-law)
    # for brother-in-law inLawsGender = 'Male' & wifeORhusband = 'Female'
    # brother-in-law ---> Spouse’s brothers, Husbands of siblings
    # for sister-in-Law inLawsGender = 'Female' & wifeORhusband = 'Male'
    # sister-in-Law ---> Spouse’s sisters, Wives of siblings
    def find_in_laws(self, name, inLawsGender, wifeORhusband):
        inLaws = []
        sibling = []
        spouseOfSibling = []
        currParent = self.member.parent

        if self.member.spouseName == name:
            sibling = self.find_siblings(inLawsGender)

        else:
            for child in currParent.children:
                if (child.name != self.member.name) and \
                        (child.gender == wifeORhusband):
                    if child.spouseName is not None:
                        spouseOfSibling.append(child.spouseName)

        inLaws = sibling + spouseOfSibling
        return inLaws
