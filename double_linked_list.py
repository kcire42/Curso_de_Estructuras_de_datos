from crear_node import Node

class TwoWayNode(Node):

    def __init__(self, data , next=None , previous=None ) -> None:
        super().__init__(data, next)
        self.previous = previous

  


if __name__ == '__main__':
    head = TwoWayNode(1)
    tail = head
    for data in range(2,6):
        tail.next = TwoWayNode(data,tail)
        tail = tail.next

    probe = tail

    while probe !=None:
        print(probe.data)
        probe = probe.previous

