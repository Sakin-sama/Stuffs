import turtle
import random
import math
from turtle import *
def dist(x1, y1, x2, y2, turtle):
  if not ((x1 - x2) == 0):
    var = (y1 - y2) / (x1 - x2)
  else:
    var = 1
  if x1 < x2:
    turtle.setheading((180 + (math.degrees(math.atan(var)))))
  else:
    turtle.setheading((math.degrees(math.atan(var))))
def compare(number1,number2):
  if (round(tx)/10)*10 == (round(number1/10))*10 and (round(ty/10))*10 == (round(number2/10))*10:
    return 1
  else:
    return 0
def walls(x,y,turtle):
  if y + 5 > HEIGHT:
    turtle.goto(x, y - 10)
  if x + 5 > WIDTH:
    turtle.goto(x - 10, y)
  if y - 5 < -HEIGHT:
    turtle.goto(x, y + 10)
  if x - 5 < -WIDTH:
    turtle.goto(x + 10, y)
def w():
  global hd
  global tx
  global ty
  t.setheading(90)
  t.goto(tx, ty + 10)
  hd = 2
def a():
  global hd
  global tx
  global ty
  t.setheading(180)
  t.goto(tx - 10, ty)
  hd = 3
def s():
  global hd
  global tx
  global ty
  t.setheading(270)
  t.goto(tx, ty - 10)
  hd = 4
def d():
  global hd 
  global tx
  global ty
  t.setheading(0)
  t.goto(tx + 10, ty)
  hd = 1
WIDTH = 330
HEIGHT = 330
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.lt(90)
hd = 1
kimagure = turtle.Turtle()
kimagure.shape("arrow")
kimagure.speed(100)
kimagure.penup()
kimagure.fillcolor("blue")
kimagure.hideturtle()
blinky = turtle.Turtle()
blinky.speed(10)
blinky.shape("arrow")
blinky.fillcolor("#FF0000")
pinky = turtle.Turtle()
pinky.speed(10)
pinky.shape("arrow")
pinky.fillcolor("#FFB8FF")
inky = turtle.Turtle()
inky.speed(10)
inky.shape("arrow")
inky.fillcolor("#00FFFF")
clyde = turtle.Turtle()
clyde.speed(10)
clyde.shape("arrow")
clyde.fillcolor("#FFB852")
blinky.penup()
pinky.penup()
inky.penup()
clyde.penup()
t.speed(1000)
t.goto(WIDTH, HEIGHT)
t.pendown()
t.goto(-WIDTH, HEIGHT)
t.goto(-WIDTH, -HEIGHT)
t.goto(WIDTH, -HEIGHT)
t.goto(WIDTH, HEIGHT)
t.penup()
n1 = [1, 2, 4]
n2 = [1, 3, 4]
n3 = [1, 2, 3]
n4 = [2, 3, 4]
t.goto(0, 100)
t.speed(10)
while 1:
  tx, ty = t.pos()
  cx, cy = clyde.pos()
  listen()
  onkey(w, 'Up')
  onkey(a, 'Left')
  onkey(s, 'Down')
  onkey(d,'Right')
  cx, cy = clyde.pos()
  tx, ty = t.pos()
  px, py = pinky.pos()
  bx, by = blinky.pos()
  ix, iy = inky.pos()
  # print(tx, ty)
  walls(cx,cy,clyde)
  walls(tx,ty,t)
  walls(bx,by,blinky)
  walls(px,py,pinky)
  walls(ix,iy,inky)
    #blinky
  dist(tx,ty,bx,by,blinky)
  blinky.fd(8)
  #pinky
  dist(tx,ty,px,py,pinky)
  match hd:
    case 1:
      pinky.setheading(pinky.heading() - 50)
      pinky.fd(12)
    case 2:
      pinky.fd(8)
    case 3:
      pinky.setheading(pinky.heading() + 50)
      pinky.fd(12)
    case 4:
      pinky.fd(1)
  #kimagure
  if blinky.heading() > 0 and blinky.heading() < 90:
    kimagure.goto(bx + 150, by + 150)
  if blinky.heading() > 90 and blinky.heading() < 180:
    kimagure.goto(bx - 150, by + 150)
  if blinky.heading() > 180 and blinky.heading() < 270:
    kimagure.goto(bx - 150, by - 150)
  if blinky.heading() > 270 and blinky.heading() < 360:
    kimagure.goto(bx + 150, by - 150)
  if blinky.heading() == 0:
    kimagure.goto(bx + 150, by)
  if blinky.heading() == 90:
    kimagure.goto(bx, by + 150)
  if blinky.heading() == 180:
    kimagure.goto(bx - 150, by)
  if blinky.heading() == 270:
    kimagure.goto(bx, by - 150)
  #inky
  kx, ky = kimagure.pos()
  dist(kx,ky,ix,iy,inky)
  inky.fd(12)
  #clyde
  dis = math.sqrt((tx - cx)**2 + (ty - cy)**2)
  if dis > 85:
    dist(tx, ty, cx, cy, clyde)
    clyde.fd(12)
  else:
    clyde.setheading(random.uniform(0, 360))
    clyde.fd(10)
  print(round(tx),round(bx),round(ty),round(by))
  if compare(bx,by) == 1 or compare(px,py) == 1 or compare(ix,iy) == 1 or compare(cx,cy) == 1:
    blinky.hideturtle()
    pinky.hideturtle()
    inky.hideturtle()
    clyde.hideturtle()
    t.pendown()
    t.pencolor("red")
    t.write("GAME OVER", font=("Arial", 30, "normal"))
    for i in range(25):
      t.setheading(random.uniform(1,360))
      t.fd(random.uniform(15,30))
    break