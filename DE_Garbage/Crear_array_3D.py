import random
from crear_array import array

class array_3D():


    def __init__(self,rows,columns,depths, fill_value =None)-> None:
        self.data = array(rows) 
        for row in range(rows):
            self.data[row] = array(columns)
            for column in range(columns):
                self.data[row][column] = array(depths,fill_value)


    def __get_height__(self):
        return len(self.data)
    

    def __get_width__(self):
        return len(self.data[0])

    def __get_depth__(self):
        return len(self.data[0][0])

    def __str__(self) -> str:
        result = ""
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                for depth in range(self.__get_depth__()):
                    result += str(self.data[row][col][depth]) + " "
                result += "\n"
        return str(result)

    
    def __random_numbers__(self):
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                for depth in range(self.__get_depth__()):
                    self.data[row][col][depth] = random.randint(10,20)

    
if __name__ == '__main__':
    matrix = array_3D(5,5,5)
    print(matrix.__get_height__())
    print(matrix.__get_width__())
    matrix.__random_numbers__()
    print(matrix.__str__())
    print(matrix.__getitem__(0)[2])


    




