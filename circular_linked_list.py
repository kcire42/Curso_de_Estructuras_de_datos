#DEFINIMOS NUESTRA CIRCULAR LINKED LIST
from itertools import count
from platform import node
from node import Node


class Circular_Linked_List:

    def __init__(self,nodes = None)->None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            #head_node = head_node.copy(self.head)
            for element in nodes:
                #print(element)
                node.next = Node(data=element)
                node = node.next
            # print(node)
            # print(self.head)
            node.next = self.head
              

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(nodes[0])
        return "-> ".join(nodes)

    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield  node
            node = node.next


    def __add_after__(self,target,new_value):
        new_node = Node(new_value)
        for node in self:
            if node.data == target:
                new_node.next = node.next
                node.next = new_node
                break


    def __add_before__(self,target,new_value):
        new_node = Node(new_value)
        temp_node = self.head
        for node in self:
            if node.data == target:
                temp_node.next = new_node
                new_node.next = node
                # print(temp_node)
                # print(node)
                break
            temp_node = node
        
    def __delete__(self,target):
        temp_node = self.head
        for node in self:
            if node.data == target:
                temp_node.next = node.next
                break
            temp_node = node

    


if __name__ == '__main__':
    # llist = Circular_Linked_List()
    # first = Node("A")
    # second = Node("B")
    # third = Node("C")
    # llist.head = first
    # first.next = second
    # second.next = third
    # third.next = llist.head
    # count = 0 
    # for element in llist:
    #     print(element)
    #     count += 1
    #     if count == 3:
    #         break
    llist_1 = Circular_Linked_List(["B","C","D","E","F"])
    llist_1.__add_after__("D","D1")
    count = 0
    for element in llist_1:
        print(element)
        count += 1
        if count == 6:
            break
    print("######################")
    llist_1.__add_before__("D","D0")
    count_1 = 0
    for element in llist_1:
        print(element)
        count_1 += 1
        if count_1 == 7:
            break
    print("######################")
    llist_1.__delete__("D0")
    count_2 = 0
    for element in llist_1:
        print(element)
        count_2 += 1
        if count_2 == 6:
            break
    
    

    
    
    
