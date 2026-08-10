class testClass:
    """testclass"""
    name = "augustus"
    
    def add_To_List(self, value):
        self.list.append(value)

    def __init__(self,number):
        self.x = number    #instance variables
        self.list = []     #instance variables




def main():
    
    print(testClass.name)
    print(testClass.__doc__)
    
    x = testClass(45)
    print(x.x)

    y = testClass(54)
    print(str(y.x) + " " + y.name)

    green = testClass(1)
    blue = testClass(1)
    print(green.list)
    print(blue.list)
    blue.add_To_List(54)
    print(green.list)
    print(blue.list)


    
main()