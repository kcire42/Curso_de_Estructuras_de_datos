from unittest import result
from array_1D import Array

class Array_2D:

    def __init__(self,rows,columns,fill_value = None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns,fill_value) 

    def __get_rows__(self):
        return len(self.data)
    
    def __get_columns__(self):
        return len(self.data[0])
        
    def __str__(self) -> str:
        result = ""
        for row in range(self.__get_rows__()):
            for column in range(self.__get_columns__()):
                result += str(self.data[row][column]) + " "
            result += "\n"
        return str(result)

    def __insertion_elements__(self):
        for row in range(self.__get_rows__()):
            for column in range(self.__get_columns__()):
                self.data[row][column] = input(f"Inserte el elemento de la posicion {row} {column}: ")




if __name__ == '__main__':
    prueba = Array_2D(2,3)
    print(prueba.__get_rows__())
    print(prueba.__get_columns__())
    print(prueba.__str__()) 
    prueba.__insertion_elements__()
    print(prueba.__str__()) 
       


