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

    
                