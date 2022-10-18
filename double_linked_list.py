from multiprocessing import dummy
from node_two_directions import Node

class Double_Linked_List:

    def __init__(self,nodes = None)-> None:
        self.head = None
        self.next = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node_2 = node.next
                node_2.previous = node
                node = node.next
    
    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "-> ".join(nodes)

    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield  node
            node = node.next

    def __find__(self,target_node):
        for node in self:
            if node.data == target_node:
                print(f"nodo previo {node.previous} nodo actual {node.data} node posterior {node.next}")

    def __add_after__(self,target_node,new_node):
        new_node = Node(new_node)
        if self.head is None:
            raise Exception ("LA DOUBLE LINK LIST ESTA VACIA")
        else:
            for node in self:
                if node.data == target_node:
                    new_node.next = node.next
                    node.next = new_node
                    new_node.previous = node
                    test = new_node.next
                    test.previous = new_node

    def __add_before__(self,target_node,new_node):
        new_node = Node(new_node)
        if self.head is None:
            raise Exception ("LA DOUBLE LINK LIST ESTA VACIA")
        else:
            for node in self:
                if node.data == target_node:
                    before_node = node.previous
                    before_node.next = new_node
                    new_node.previous = before_node
                    new_node.next = node
                    node.previous = new_node


    def __delete__(self,target_node):
        if self.head is None:
            raise Exception ("LA DOUBLE LINK LIST ESTA VACIA")
        else:
            for node in self:
                if node.data == target_node:
                    after_node = node.next
                    before_node = node.previous
                    before_node.next = after_node
                    after_node.previous = before_node




    
if __name__ == '__main__':
    llist_1 = Double_Linked_List(["B","C","D","E","F"])
    llist = Double_Linked_List()
    first = Node("A")
    llist.head = first
    second = Node("B")
    first.next = second
    second.previous = first
    third = Node("C")
    second.next = third
    third.previous = second
    print(llist)
    print(llist_1)
    llist_1.__find__("D")
    llist_1.__add_after__("D","D1")
    print(llist_1)
    llist_1.__find__("F")
    llist_1.__add_before__("D","D0")
    print(llist_1)
    llist_1.__find__("D0")
    llist_1.__delete__("D0")
    print(llist_1)
    
                