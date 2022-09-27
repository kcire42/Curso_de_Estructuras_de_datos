
import random


class array:
        def __init__(self,capacity,fill_value = None):
            self.capacity = capacity
            self.items =list()
            for i in range(capacity):
                self.items.append(fill_value)

        def __len__(self):
            return len(self.items)
    

        def __str__(self) -> str:
            return str(self.items)

    
        def __iter__(self):
            return iter(self.items)

        def __getitem__(self,index):
            return self.items[index]

        def __setitem__(self,index,new_item):
            self.items[index] = new_item

        def reverse_items(self):
            return self.items[::-1]
    
        def __str__(self) -> str:
            return str(self.items)


class Array_2D():

    def __init__(self,rows , columns, fill_value = None) -> None:
        self.data = array(rows)
        for row in range(rows):
            self.data[row] = array(columns,fill_value)

    
    def __get_height__(self): #Altura de array
        return len(self.data)
    

    def __get_width__(self): #Ancho de array
        return len(self.data[0])

    
    def __str__(self) -> str:
        result = ""
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

    def __add_elements__(self,elements):
        print(elements)
        # for element in elements:
        #     for ele in element:
        #         print(ele)
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                self.data[row][col] = elements[row][col]
            
       
        

            




if __name__ == '__main__':

    arr = []
    height = 4
    
    for _ in range(height):
        arr.append(list(map(int,input().rstrip().split())))
    width = len(arr[0])
    matrix = Array_2D(height,width)
    print(matrix.__get_height__())
    print(matrix.__get_width__())
    matrix.__add_elements__(arr)
    print(matrix.__str__())
        

    