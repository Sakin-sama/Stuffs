import turtle
import math
import random

t = turtle.Turtle()
t.fillcolor("green")
t.shape("turtle")
t.penup()
t.pencolor("green")
t.goto(-200,100)

q = turtle.Turtle()
q.fillcolor("blue")
q.pencolor("blue")
q.shape("turtle")
q.penup()
q.goto(-200,-100)

t.goto(200,60)
t.pendown()
t.circle(40)
t.penup()
t.goto(-200,100)

q.goto(200,-140)
q.pendown()
q.circle(40)
q.penup()
q.goto(-200,-100)

d = [1,2,3,4,5,6]

for i in  range(19):
  if t.pos() >= (200,100):
    print("Player 1 wins!")
    break

  elif q.pos() >= (200,-100):
    print("Player 2 wins!")
    break
  
  print("press enter", input())
  if input() == "":
    er = random.choice(d)
    print("die roll:",er)
    print("move forwards:",20*er)
    t.forward(20*er)
  
  print("press enter player 2", input())
  if input() == "":
    kr = random.choice(d)
    print("die roll:",kr)
    print("move forwards:",20*kr)
    q.forward(20*kr)
  








