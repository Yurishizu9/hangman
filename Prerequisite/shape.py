class Shape():
    def __init__(self, num_sides, tesselates = None):
        self.num_sides = num_sides
        self.tesselates= tesselates
        if self.num_sides == 0:
            raise ValueError('must be bigger than 0')
        
    def get_info(self):
        '''
        this is an "abstract base class", which means it should only be used when inherited 
        from by other classes. There should be no instances of this generic Shape class
        '''
        raise ModuleNotFoundError 
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'

    def __str__(self):
        return self.get_info()

    def __add__(self, other_shape):
        return self.num_sides + other_shape.num_sides


class Circle(Shape):
    def __init__(self):
        super().__init__(1)

    def get_info(self):
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'
    


class Triangle(Shape):
    def __init__(self):
        super().__init__(3)

    def get_info(self):
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'

class Square(Shape):
    def __init__(self):
        super().__init__(4)

    def get_info(self):
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'

class Pentagon(Shape):
    def __init__(self):
        super().__init__(5)

    def get_info(self):
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'


class Hexagon(Shape):
    def __init__(self):
        super().__init__(6)

    def get_info(self):
        return f'Number of Sides: {self.num_sides}, Tesselates: {self.tesselates}'


gen_shape = Shape(9)
cir = Circle()
tri = Triangle()
print(cir + tri)

'''
Why is it that  an instance of the child class can bypass Line 13: raise ModuleNotFoundError 
But an instance of the base class cannot
'''
print(cir) # >>> Number of Sides: 1, Tesselates: None
print(gen_shape) # >>> ModuleNotFoundError

