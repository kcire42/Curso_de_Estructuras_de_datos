#DEFINIMOS NUESTRA CIRCULAR LINKED LIST
from node import Node


class Circular_Linked_List:

    def __init__(self,nodes = None)->None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            #head_node = head_node.copy(self.head)
            for element in nodes:
                node.next = Node(data=element)
                node.next
            node.next = self.head
            

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
    llist1 = Circular_Linked_List(["B","C","D","E","F"])
    print(llist1)