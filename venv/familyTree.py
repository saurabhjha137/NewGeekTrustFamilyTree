# stucture of each Node in Family Tree


class FamilyTreeNode:
    # initializes node with parameters passed
    # from GenerateTree.create_member_nodes()
    def __init__(self, name, gender, spouseName=None, spouseGender=None):
        self.name = name
        self.gender = gender
        self.spouseName = spouseName
        self.spouseGender = spouseGender
        self.children = []
        self.parent = None

    # adds child to RootMember
    # child will be appended to list children of RootMember
    def add_child_node(self, child):
        child.parent = self
        self.children.append(child)

    # returns level of the node to be used, to print Family Tree
    def get_node_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent

        return level

    # check if member has spouse or not i.e married or not
    def if_member_is_married(self):
        return self.spouseName is not None

    # check if node == female and nodeName == mothername
    def if_parent_is_mother(self, motheName):
        return (self.name == motheName and self.gender == 'Female') or \
                (self.spouseName == motheName and self.spouseGender == 'Female')

    # ---------can be used to print the tree ---------#
    def print_family_tree(self):
        spaces = '    ' * self.get_node_level() * 3
        prefix = spaces + "--> " if self.parent else " "
        if self.spouseName is None:
            print(prefix + self.name + ' ' + self.gender + "\n")
        else:
            print(prefix + self.name + ' ' + self.gender + ' + ' +
                  self.spouseName + ' ' + self.spouseGender + "\n")

        if self.children:
            for child in self.children:
                child.print_family_tree()

    # ---------------------  ***  ---------------------#
