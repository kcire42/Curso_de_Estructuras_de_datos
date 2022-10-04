#DEFINIMOS NUESTRA LINKED LIST
from node import Node


class Linked_List:
    def __init__(self,nodes = None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next


    #FUNCION PARA EL RETORNO DE STR 
    
    def __str__(self) -> str:
        """REGRESA EL CONTENIDO DE MI LINKED LIST EN STR Y LA POSICION DE COMO VAN ORDENADAS"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "-> ".join(nodes)
    

    #FUNCION PARA HACER ITERACION DEL ITER
    def __iter__(self):
        """FUNCION QUE REGRESA MI LINKED LIST ITERANDO LOS ELEMENTOS"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __insert_first_pos__(self,new_value):
        node = Node(new_value)
        node.next = self.head
        self.head = node 
        
    def __insert_last_pos__(self,new_value):
        if self.head is None:
            self.head = new_value
            return
        for current_node in self:
            pass
        current_node.next = node
        
        



if __name__ == '__main__':
    llist = Linked_List()
    print(llist)
    first = Node("a")
    llist.head = first
    print(llist)
    second = Node("b")
    first.next = second
    print(llist)
    third = Node("c")
    second.next = third
    print(llist)
    llist_1 = Linked_List(["A","B","C","D","E"])
    print(llist_1)
    for node in llist_1:
        print(node)
    print(llist_1)
    llist_1.__insert_first_pos__("F")
    print(llist_1)
    llist_1.__insert_last_pos__("F")
    print(llist_1)