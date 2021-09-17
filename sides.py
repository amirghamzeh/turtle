import turtle

sides = int(input("Enter number of sides: "))

angle = 180 - (((sides - 2) * 180) / sides)


for i in range(sides):
    turtle.forward(100)
    turtle.left(angle)

input()