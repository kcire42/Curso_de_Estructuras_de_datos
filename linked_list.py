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
