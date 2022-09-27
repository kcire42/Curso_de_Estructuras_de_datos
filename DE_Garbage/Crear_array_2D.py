import random
from crear_array import array

class array_2D():
    

    def __init__(self, rows, columns, fill_value= None) -> None:
        self.data = array(rows)
        for row in range(rows):
            self.data[row] = array(columns,fill_value)

    
    def __get_height__(self):
        return len(self.data)

    def __get_width__(self):
        return len(self.data[0])

    def __getitem__(self,index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

    def __random_numbers__(self):
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                self.data[row][col] = random.randint(0,9)


if __name__ == '__main__':
    matrix = array_2D(5,5)
    print(matrix.__get_height__())
    print(matrix.__get_width__())
    matrix.__random_numbers__()
    print(matrix.__str__())
    print(matrix.__getitem__(0)[2])



