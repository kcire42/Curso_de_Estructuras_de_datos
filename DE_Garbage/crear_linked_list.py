from itertools import count
from crear_node import Node
from crear_array import array


class linked_list:

    def __init__(self) -> None:
        self.tail = None  # es none por que es el ultimo nodo
        self.size = 0  # 0 por que no hay nodos

    def __append__(self, data):
        # Entra un dato y con mi clase nodo creo un nodo ocn un valor y un puntoro como none
        node = Node(data)
        if self.tail == None:
            self.tail = node  # si no hay nodos en mi lista voy a decir que mi colo es igual al primer nodo por que no habia nodos
        else:
            current = self.tail  # pero si hay nodo voy decir que mi estado actual es donde esta mi cola

            while current.next:  # mientras que haya algo que iterar avanzo
                current = current.next  # como hay algo avanzo a la siguiente posicion de memoria

            # y eso que avanze ahi coloco mi nuevo nodo bien bonito y aumento en 1 el tamaño de mi lista
            current.next = node

        self.size += 1

    def __size__(self):
        return str(self.size)

    def __iter__(self):
        current = self.tail  # me voy al final de mi lista
        while current:  # mientra que haya algo en current
            val = current.data  # mi valor actual donde estoy

            current = current.next  # avanzo  a mi siguiente valor
            yield val  # regeso el valor donde estoy

    def __delete__(self, data):
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

    def __search__(self, data):

        for node in self.__iter__():
            if data == node:
                print(f"Data {data} found")

    def __clear__(self):
        self.tail = None
        self.head = None
        self.size = 0


# Metodo par verificar si tengo un elemento en mi lista

    def __verify_element__(self, element):
        current = self.tail
        while current != None and current.data != element:
            #count = 0 
            print(current.data)
            #Forma de encontra elemento por contadores funciona pero no esta bonito 
            # if current.data == element:
            #     print(f"El elemento {element} si se encuentra en la lista")
            #     break
            # else:
            #     count += 1
            current = current.next
        #print(current)
        # if count == 1:
        #    print(f"El elemento {element} no se encuentra en la lista")
        if current != None:
            print(f"El elemento {element} si se encuentra en la link list con una ubicacion de {current}")
        else:
            print(f"El elemento {element} no se encuentra en la link list {current}")                     

# Metodo para  reemplazar

    def __replace_element__(self, old_element ,new_element):
        current = self.tail
        while  current != None and current.data != old_element:
            current = current.next
        if current != None:
            current.data = new_element

# Insertar un elemento al inicio de mis lista
    def __insert_element__(self, new_element):
        pass


#Metodo para recorrer mis nodos 
    def __inspect_nodes__(self):
        current = self.tail
        while  current:
            print(current.data)
            current = current.next



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
    # print(words.__str__())
    list_of_words = linked_list()
    for i in range(words.capacity):
        # print(words.__getitem__(i))
        list_of_words.__append__(words.__getitem__(i))
    list_of_words.__verify_element__("hola")
    list_of_words.__verify_element__("c")
    list_of_words.__inspect_nodes__()
    list_of_words.__replace_element__("c","h")
    list_of_words.__inspect_nodes__()
    # current = list_of_words.tail
    # while current:
    #     print(current.data)
    #     current = current.next
    # print(list_of_words.__iter__())
