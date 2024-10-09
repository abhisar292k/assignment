class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(5, 10)
for dimension in rect:
    print(dimension)

# Output:
# {'length': 5}
# {'width': 10}

#The __init__ method initializes the length and width properties when an instance is created.
#The __iter__ method is defined to allow iteration over the object. 
# It first yields the length as a dictionary, then the width