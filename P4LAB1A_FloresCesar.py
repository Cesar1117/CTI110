#Flores Cesar
#04/28/2024
#P4 LAB1
#Use turtle and loops to draw a square
import turtle
win = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.pencolor("green")
pen.shape("turtle")
for side in range (4) :
    pen.forward(100)
    pen.left(90)
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides -1

win.mainloop()