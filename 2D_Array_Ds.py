


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

    
    def __get_height__(self):
        return len(self.data)
    

    def __get_width__(self):
        return len(self.data[0])

    
    def __str__(self) -> str:
        result = ""
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)



if __name__ == '__main__':
    matrix = Array_2D(6,6)
    print(matrix.__str__())
        

    