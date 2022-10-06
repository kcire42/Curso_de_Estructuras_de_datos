#DEFINIMOS NUESTRA CLASE NODO CON LA INTENCION DE TENER DOS NODOS
"""CLASE NODO QUE TIENE LA CARACTERISITICA DONDE
TENEMOS UNA DIRECCION ANTERIOR Y POSTERIOR"""

class Node:
    
    def __init__(self,data) -> None:
        self.previous = None
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)