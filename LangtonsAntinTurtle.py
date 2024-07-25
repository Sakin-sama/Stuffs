import turtle
import time


WIDTH = 1000
HEIGHT = 1000
s = turtle.Screen()
s.setup(WIDTH, HEIGHT)

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(1)
t.speed(0)
t.penup()
s.bgcolor("white")
t.pensize(15)

b = {}

while 1:
  time.sleep(0)
  
  if (round(t.xcor()),round(t.ycor())) in b.keys():
    t.pendown()
    t.pencolor("white")
    del b[(round(t.xcor()),round(t.ycor()))]
    t.rt(-90)
    t.forward(15)
   
    t.penup()
  else:
    t.pendown()
    t.pencolor("black")
    b[(round(t.xcor()),round(t.ycor()))] = "black"
    t.rt(90)
    t.fd(15)
   
    t.penup()
  # print(b)
  # print(t.heading())
  # print(t.pos())
  
