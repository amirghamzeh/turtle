from shape import Shape
import math

class Triangle(Shape):

    def __init__(self, side):
        super()

        side2 = math.sqrt(2 * (side * side))
        self.paths = [(side, 45), (side2, 45), (side, 90)]