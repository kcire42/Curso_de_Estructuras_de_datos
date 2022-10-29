from dbm import dumb
from inspect import stack
from node import Node

class Stacks:

    def __init__(self,nodes = None) -> None:
        self.superior = None
        self.next = None
        if nodes is not None:
            node = Node (data = nodes.pop(0))
            self.superior = node
            print("Nodo Ok")
            for element in nodes:
                print("next_node")
                new_node = Node(data = element)
                new_node.next = self.superior
                self.superior = new_node





    def __str__(self) -> str:
        node = self.superior
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "\n|\n".join(nodes)

    def __iter__(self):
        node = self.superior
        while node is not None:
            yield node
            node = node.next

    def __add__(self, new_value):
        new_node = Node(new_value)
        if self.superior == None:
            self.superior = new_node
            return
        else:
            new_node.next = self.superior
            self.superior = new_node

    def __lifo__ (self):
        return "El primero en la pila es "+str(self.superior)
    
    def __delete_any_item__(self,target_value):
        dummy = self.superior
        for element in self:
            #print(element.data)
            if element.data == target_value:
                dummy.next = element.next
            dummy = element
    #Last in first out
    def __delete_lifo__(self):
        first = self.superior
        print(first.data)
        first = first.next
        print(first)
        




if __name__ == '__main__':
    # stacks = Stacks()
    # first = Node("A")
    # stacks.head = first
    # print(stacks)
    # stacks.__add__("B")
    # print(stacks)
    # stacks.__add__("C")
    # print(stacks)
    stacks_1 = Stacks(["A","B","C","D","E","F"])
    print(stacks_1)
    #print(stacks_1.__lifo__())
    print("////////////////////////////")
    stacks_1.__delete_any_item__("B")
    print(stacks_1)
    print("////////////////////////////")
    stacks_1.__delete_lifo__()
    
    print(stacks_1)