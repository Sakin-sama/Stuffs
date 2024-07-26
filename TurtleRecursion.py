import turtle
import random

b = turtle.Turtle()
b.shape("turtle")
b.speed(1000000)
WIDTH = 1000
HEIGHT = 1000
s = turtle.Screen()
s.screensize(WIDTH, HEIGHT)
b.pensize(2)
s.bgcolor("black")


def draw(n, color, f):
  if (n < 10):
    # print("return")
    return
  else:

    b.pencolor(color)
    b.forward(n)
    b.left(30)

    # print(n,"1")

    draw(f * n / (f + 1), color, f)
    #line 8 start
    # print(n,"2")
    b.rt(60)

    draw(f * n / (f + 1), color, f)
    #line 15 start
    # print(n,"3")

    b.lt(30)

    b.backward(n)

    # print(n,"4")


def fibonacci(n):
  num = []
  for i in range(n):
    if i == 0:
      num.append(0)

    elif i == 1:
      num.append(1)
    else:
      num.append(num[i - 2] + num[i - 1])
  print(num)

  return num[n - 1]


y = 3
c = ["yellow", "magenta", "red", "#FFF8DC", "lightgreen", "cyan"]
f1 = [3, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6]
g1 = [4, 4, 4, 4, 5, 5, 5, 5, 7, 7, 7, 7]
for x in range(32):
  for w in range(4):
    draw(40, random.choice(c), fibonacci(y))
    b.rt(90)

  y = y + 1
