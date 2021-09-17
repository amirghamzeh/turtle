import turtle
import random

class Shape:

    paths = []

    def draw(self):
        turtle.shape('turtle')
        colors = ['red', 'green', 'blue', 'black']
        for path in self.paths:
            turtle.pencolor(random.choice(colors))
            turtle.speed(1)
            turtle.pensize(5)
            turtle.forward(path[0])
            turtle.left(180 - path[1])