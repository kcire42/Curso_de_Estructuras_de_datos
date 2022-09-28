#CREACION DE UN ARRAY 
#LO PRIMERO QUE DEBO DE HACER ES DEFINIR MI CLASE DONDE TENDRE MI ESTRUCTURA DE DATOS 


class Array:
    
    def __init__(self,length,fill_value = None) -> None:
        self.length = length #defino la longitudo de mi array
        self.items = list() #declaro mi lista donde guardare mis elementos
        for element in range(length): #hago el llenado de mi elementos
            self.items.append(fill_value)
    
    def __len__(self)->int:
        return len(self.items)
    
    # def __insertion_by_index__(self,index,new_value):
    #     self.items[index] = new_value
    
    def __setitem__(self,index,new_item):
            self.items[index] = new_item
    
    def __getitem__(self,index):
            return self.items[index]

    def __insertion_multiple_value__(self):
        for element in range(len(self.items)):
            self.items[element] = int(input("Ingrese un valor: "))

    def __delete_element__(self,value):
        for i in range(len(self.items)):
            if self.items[i] == value:
                self.items[i] = None

    def __search_element__(self,value):
        if value in self.items:
            print(f"El valor {value} si se encuentra en el array")
        else:
            print("El valor no se encuentra en el array")

    def __replace_element__(self,value,new_value):
        for i in range(len(self.items)):
            if self.items[i] == value:
                self.items[i] = new_value

    def __print_by_element__(self):
        for element in self.items:
            print(element)
            
            

    
    def __str__(self) -> str:
        return str(self.items)






# if __name__ == '__main__':
#     estacionamiento = Array(5)
#     print(estacionamiento.__len__())
#     #estacionamiento.__insertion_by_index__(0,5)
#     estacionamiento.__insertion_multiple_value__()
#     print(estacionamiento.__str__())
#     estacionamiento.__delete_element__(3)
#     print(estacionamiento.__str__())
#     estacionamiento.__search_element__(2)
#     estacionamiento.__search_element__(6)
#     estacionamiento.__print_by_element__()
#     estacionamiento.__replace_element__(1,6)
#     print(estacionamiento.__str__())

