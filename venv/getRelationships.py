from findRelations import FindRelationship

class GetRelationship:
    # initializes relation to FindRelationship Class
    def __init__(self, member):
        self.relation = FindRelationship(member)

    # returns paternal uncle
    def get_paternal_uncle(self,
                           maternalORpaternal='Male',
                           uncleORaunty='Male'):
        return self.relation.find_uncle_aunty(maternalORpaternal, uncleORaunty)

    # returns paternal aunty
    def get_paternal_aunty(self,
                           maternalORpaternal='Male',
                           uncleORaunty='Female'):
        return self.relation.find_uncle_aunty(maternalORpaternal, uncleORaunty)

    # returns maternal uncle
    def get_maternal_uncle(self,
                           maternalORpaternal='Female',
                           uncleORaunty='Male'):
        return self.relation.find_uncle_aunty(maternalORpaternal, uncleORaunty)

    # returns maternal aunty
    def get_maternal_aunty(self,
                           maternalORpaternal='Female',
                           uncleORaunty='Female'):
        return self.relation.find_uncle_aunty(maternalORpaternal, uncleORaunty)

    # returns sister in law
    def get_sister_in_law(self,
                          name,
                          inLawsGender='Female',
                          wifeORhusband='Male'):
        return self.relation.find_in_laws(name, inLawsGender, wifeORhusband)

    # returns brother in law
    def get_brother_in_law(self,
                           name,
                           inLawsGender='Male',
                           wifeORhusband='Female'):
        return self.relation.find_in_laws(name, inLawsGender, wifeORhusband)

    # returns daughter
    def get_daughters(self, siblingGender='Female'):
        return self.relation.find_siblings(siblingGender)

    # returns son
    def get_sons(self, siblingGender='Male'):
        return self.relation.find_siblings(siblingGender)

    # returns siblings by merging son and daughter
    def get_siblings(self):
        son = self.get_sons()
        daughter = self.get_daughters()
        return daughter + son