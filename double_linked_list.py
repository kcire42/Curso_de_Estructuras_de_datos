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

    
                