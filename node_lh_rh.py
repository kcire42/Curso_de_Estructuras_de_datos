#NODO QUE TIENE POSICION IZQUIERDA Y POSICION DERECHA
class Node:

    def __init__(self,data,parent = None) -> None:
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    

    def __str__(self) -> str:
        return str(self.data)

        