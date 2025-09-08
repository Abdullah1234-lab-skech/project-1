import turtle
screen = turtle.Screen()
screen.bgcolor('blue')
screen.setup(400, 500)
Square = turtle.Turtle()
length = 90
angle = 90
for i in range(4):
    Square.forward(length)
    Square.right(angle)
turtle.done()