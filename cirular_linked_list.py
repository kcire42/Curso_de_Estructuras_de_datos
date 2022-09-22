from crear_array import array
from crear_node import Node
from crear_linked_list import linked_list

class cirular_linked_list(linked_list):

    def __init__(self) -> None:
        super().__init__()
    
    def __append__(self, data, next = None):
        node = Node(data, next)
        if self.tail == None:
            self.tail = node  # si no hay nodos en mi lista voy a decir que mi colo es igual al primer nodo por que no habia nodos
            self.tail.next = self.tail
        else:
            node.next = self.tail
            current = self.tail  # pero si hay nodo voy decir que mi estado actual es donde esta mi cola
            
            while current.next != self.tail:  # mientras que haya algo que iterar avanzo
                current = current.next  # como hay algo avanzo a la siguiente posicion de memoria

            # y eso que avanze ahi coloco mi nuevo nodo bien bonito y aumento en 1 el tamaño de mi lista
            current.next = node

        self.size += 1
      

    def __print__(self):
        current = self.tail
        node_number = self.size
        while  node_number > 0:
            print (f'The Node {current} have value {current.data}')
            current = current.next
            node_number -= 1

    

    



if __name__ == '__main__':
    words = array(5)
    words.__insert_elements__()
    # print(words.__str__())
    circle_words = cirular_linked_list()
    for i in range(words.capacity):
        # print(words.__getitem__(i))
        circle_words.__append__(words.__getitem__(i))
    
    circle_words.__print__()
   
 


