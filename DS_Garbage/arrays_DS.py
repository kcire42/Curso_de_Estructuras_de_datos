




class Array:

    def __init__(self,capacity,fill_value = None) -> None:
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    

    def set_item(self,index,new_item):
        self.items[index] = new_item

    def reverse_items(self):
        #reverse_array = " ".join(map(str,self.items[::-1]))
        return self.items[::-1]
    
    def __str__(self) -> str:
        return str(self.items)


def reverseArray(array_count,list_of_elements):
    array = Array(array_count)
    print(array.__str__())
    for i in range(array_count):
        array.set_item(i,list_of_elements[i])
    # return array.reverse_items()
    print(array.__str__())
    print(array.reverse_items())
    test = "6762 8850 586 423 8373 4063 3216 6676"
    if array.reverse_items() == test:
        print(True)
    else:
        print(False)
        
        




if __name__ == '__main__':

    array_count = int(input().strip())
    list_of_elements = list(map(int, input().rstrip().split()))
    # print(reverseArray(array_count,list_of_elements))
    reverseArray(array_count,list_of_elements)