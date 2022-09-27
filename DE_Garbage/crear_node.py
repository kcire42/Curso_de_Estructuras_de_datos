

class Node():


    def __init__(self,data,next= None) -> None:
        self.data = data
        self.next = next

if __name__ == '__main__':
    nodo_1 = Node("C",None)
    #nodo_1 = None
    #nodo_2 = Node("A" , None)
    nodo_2 = Node("A" , nodo_1)
    nodo_3 = Node("B" , nodo_2)
    print(nodo_2.data)
    print(nodo_2.next.data)
    print(nodo_3.data)
    print(nodo_2.next.data)
    head = None
    for count in range (1,5):
        head = Node(count,head)

    # for element in head: aqui pude ver algo interesante no se puede recorrer como una lista un nodo 
        # print(head.next.data)
    while head != None:
        print(head.data)
        head= head.next
        

        