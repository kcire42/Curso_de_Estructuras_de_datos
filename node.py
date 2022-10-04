
#DEFINIMOS NUESTRA CLASE NODO 

class Node:
    """CREACION DE NODO REQUIERE UN PARAMETRO DE DATO Y CUANDO SE CREA EL NODO APUENTA A NONE"""
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


