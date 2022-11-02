from node import  Node

class Queues:

    def __init__(self,nodes = None) -> None:
        self.head = None
        self.next = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                new_node = Node(data=element)
                node.next = new_node
                node = new_node


    
    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node  is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __add__(self,new_value):
        new_node = Node(new_value)
        for element in self:
            if element.next is None:
                dummy = element
        dummy.next = new_node
                
    def __fifo__(self):
        return "El primero en la fila es: " + str(self.head)

    def __delete_fifo__(self):
        self.head = self.head.next
    
    def __search__(self,target):
        for element in self:
            if target == element.data:
                print("El elemento si se encuentra")
                break
            elif element.next is None:
                print("El elemento no es encuentra")
        
       

    





if __name__ == '__main__':
    queues = Queues()
    first = Node("A")
    second = Node("B")
    queues.head = first
    first.next = second
    print(queues)
    queues_1 = Queues(["A","B","C","D","E"])
    print(queues_1)
    queues_1.__add__("F")
    print(queues_1)
    print(queues_1.__fifo__())
    queues_1.__delete_fifo__()
    print(queues_1)
    queues_1.__search__("G")
