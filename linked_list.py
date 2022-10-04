#DEFINIMOS NUESTRA LINKED LIST
from node import Node


class Linked_List:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "-> ".join(nodes)



if __name__ == '__main__':
    llist = Linked_List()
    print(llist.__str__())
    first = Node("a")
    llist.head = first
    print(llist.__str__())
    second = Node("b")
    first.next = second
    print(llist.__str__())
    third = Node("c")
    second.next = third
    print(llist.__str__())
