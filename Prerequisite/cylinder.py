import math

class Cylinder():
    '''Create a Cylinder object
    You can work out the surface area or volume by calling .get_surface_area() and .get_volume()
    Parameters
    ----------
    height : _float_
        heingt of the cylinder
    radius : _float_
        radius of the cylinder
    '''
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()


    def get_surface_area(self):
        self.surface_area = 2 * math.pi * self.radius * self.height + 2 * math.pi * math.pow(self.radius, 2)
        return f'{round(self.surface_area, 2)} cm³'


    def get_volume(self):
        self.volume = math.pi  * self.height * math.pow(self.radius, 2)
        return f'{round(self.volume, 2)} cm³'

c = Cylinder(7, 4)
print(c.get_surface_area())
print(c.get_volume())
    