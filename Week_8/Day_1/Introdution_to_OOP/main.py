class Point():
    def __init__(self, x, y): # init method need to initialize instance of class with or without user-defined attributes
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x) # output will be "p.x is: 3"
print("p.y is:", p.y) # output will be "p.y is: 4"