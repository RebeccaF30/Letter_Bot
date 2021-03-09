from turtle import *

size = 5
screen = Screen()
screen.title("Handrighting bot")
screen.screensize(400,100,"light blue")
pen = Turtle()
pen.penup()
pen.goto(-200,0)
pen.pendown()
pen.color("black")
pen.speed(10)

def x():
    sizeu=size*1.5
    pen.pendown()
    pen.left(45)
    pen.fd(sizeu * 10)
    pen.left(45+90)
    pen.penup()
    pen.fd(sizeu * 7)
    pen.pendown()
    pen.left(90+45)
    pen.fd(sizeu * 10)
    pen.left(45)
    pen.penup()
    pen.fd(sizeu * 3)

def c():
    pen.penup()
    pen.fd(size * 5)
    pen.right(-90)
    pen.fd(size * 10)
    pen.left(90)
    pen.pendown()
    for i in range(1,180):
        pen.fd(size*0.1)
        pen.left(1)
    pen.penup()
    pen.fd(size * 3)
def o():
    pen.penup()
    pen.fd(size * 5)
    pen.right(-90)
    pen.fd(size * 10)
    pen.left(90)
    pen.pendown()
    for i in range(1,360):
        pen.fd(size*0.1)
        pen.left(1)
    pen.penup()
    pen.right(-90)
    pen.fd(size * 12)
    pen.left(90)
    pen.fd(7 * size)

o()
x()