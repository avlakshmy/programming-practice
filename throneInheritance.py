class Person:
    
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isAlive = True
    
class ThroneInheritance:
    
    def __init__(self, kingName):
        king = Person(kingName)
        self.kingName = kingName
        self.people = {}
        self.people[kingName] = king

    def birth(self, parentName, childName):
        if not parentName in self.people:
            self.people[parentName] = Person(parentName)
        if not childName in self.people:
            self.people[childName] = Person(childName)
        self.people[parentName].children.append(self.people[childName])

    def death(self, name):
        self.people[name].isAlive = False

    def preorderTraversal(self, root):
        if root:
            preorder = [root]
            for child in root.children:
                preorder.extend(self.preorderTraversal(child))
            return preorder
        return []
    
    def getInheritanceOrder(self):
        root = self.people[self.kingName]
        tempOrder = self.preorderTraversal(root)
        for po in self.people:
            p = self.people[po]
        order = []
        for p in tempOrder:
            if p.isAlive:
                order.append(p.name)
        return order
