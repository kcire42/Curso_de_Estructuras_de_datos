from crear_node import Node
from crear_array import array

class linked_list:
    
    def __init__(self) -> None:
        self.tail = None #es none por que es el ultimo nodo 
        self.size = 0 #0 por que no hay nodos
    
    def __append__(self,data):
        node = Node(data) #Entra un dato y con mi clase nodo creo un nodo ocn un valor y un puntoro como none
        if self.tail == None:
            self.tail = node # si no hay nodos en mi lista voy a decir que mi colo es igual al primer nodo por que no habia nodos 
        else:
            current = self.tail #pero si hay nodo voy decir que mi estado actual es donde esta mi cola

            while current.next: #mientras que haya algo que iterar avanzo 
                current = current.next  # como hay algo avanzo a la siguiente posicion de memoria

            current.next = node #y eso que avanze ahi coloco mi nuevo nodo bien bonito y aumento en 1 el tamaño de mi lista

        self.size += 1


    def __size__(self):
        return str(self.size)

    def __iter__(self):
        current = self.tail #me voy al final de mi lista
        while current: #mientra que haya algo en current
            val = current.data #mi valor actual donde estoy
            current = current.next #avanzo  a mi siguiente valor
            yield val #regeso el valor donde estoy 

    def __delete__(self,data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail == current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            
            previous = current
            current = current.next
        

    def __search__(self,data):

        for node in self.__iter__():
            if data == node:
                print(f"Data {data} found")
    
    def __clear__(self):
        self.tail = None
        self.head = None
        self.size = 0

if __name__ == '__main__':
    # words = linked_list()
    # words.__append__("Salmon")
    # words.__append__("Atun")
    # words.__append__("Queso")
    # current = words.tail
    # while current:
    #     print(current.data)
    #     current = current.next
    # print(words.__size__())
    # words.__delete__("Queso")
    # current = words.tail
    # while current:
    #     print(current.data)
    #     current = current.next
    # print(words.__size__())
    # words.__search__("Salmon")
    words = array(5)
    words.__insert_elements__()
    print(words.__str__())
    list_of_words  = linked_list()
    for i in range(words.capacity):
        #print(words.__getitem__(i))
        list_of_words.__append__(words.__getitem__(i))
    current = list_of_words.tail
    while current:
        print(current.data)
        current = current.next
    list_of_words.__iter__()





    