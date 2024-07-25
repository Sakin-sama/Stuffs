import turtle
import random
import time
from turtle import *


turtle.tracer(0)

T_STEP = 10

lives = 5
score = 0

espeed = 1
rate = 70
ammo = 12000
max = 5000

lasers = []
enemies = []

FRAME_RATE = 30
TIME_FOR_1_FRAME = 1 / FRAME_RATE

game_timer = time.time()

colours = ["green", "red", "white", "purple", "orange", "yellow", "blue"]

def left():
    t.t_movement = -1
def right():
    t.t_movement = 1
def rleft():
    t.t_rotation = 1
def rright():
    t.t_rotation = -1
def rstop():
    t.t_rotation = 0
def stop():
    t.t_movement = 0
def q():
    turtle.done()  
def draw():
    t.clear()
    t.turtlesize(4, 1)
    t.stamp()
    t.fd(10)
    t.turtlesize(1.5, 1)
    t.stamp()
    t.fd(10)
    t.turtlesize(0.3, 0.8)
    t.stamp()
    t.fd(-20)
def laser():
    global ammo
    global max
    if ammo > 0 and len(lasers) < max:
        laser = turtle.Turtle()
        laser.penup()
        laser.color(1, 0, 0)
        laser.hideturtle()
        laser.setposition(t.xcor(), t.ycor())
        laser.setheading(t.heading())
        laser.forward(20)
        laser.pendown()
        laser.pensize(5)
        lasers.append(laser)
        ammo = ammo - 1
    else:
        return
def lasermove(laser):
    laser.clear()
    laser.penup()
    laser.fd(10)
    laser.pendown()
    laser.fd(20)
    laser.fd(-20)
def enema():
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.shape("turtle")
    random_color = random.choice(colours)
    enemy.color(random_color)
    enemy.sety(TOP)
    enemy.setx((round(random.randint(LEFT*.975, RIGHT*.975)/10))*10)
    enemies.append(enemy)
    enemy.setheading(270)
def enemymove(enemy):
    enemy.fd(espeed)
def compare(sprite1, sprite2):
    ax, ay = sprite1.pos()
    bx, by = sprite2.pos()
    if (round(ax)/10)*10 == (round(bx/10))*10 and (round(ay/10))*10 == (round(by/10))*10:
        return 1
    else:
        return 0
def remove(sprite, list):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    list.remove(sprite)
    turtle.turtles().remove(sprite)

window = turtle.Screen()
window.setup(.5,.75)
window.bgcolor('gray')

w, h = window.window_width(), window.window_height()

LEFT = -w / 2
RIGHT = w / 2
TOP = h / 2
BOTTOM = -h / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * window.window_width()

t = turtle.Turtle()
t.shape('square')
t.penup()
t.color('white')
t.speed(0)

t.sety(FLOOR_LEVEL)
t.setx(.25)

t.setheading(90)
t.turtlesize(4,1)
t.stamp()
t.fd(10)
t.turtlesize(1.5,1)
t.stamp()
t.fd(10)
t.turtlesize(0.3,.8)
t.stamp()
t.fd(-20)
t.t_movement = 0
t.t_rotation = 0

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(LEFT * .975, TOP * 0.9)
text.color(1, 1, 1)

listen()
onkey(quit, 'q')
onkeypress(left, 'Left')
onkeypress(right, 'Right')
onkeyrelease(stop, "Left")
onkeyrelease(stop, "Right")
onkey(laser, 'space')
onkeypress(rleft, "a")
onkeypress(rright,"d")
onkeyrelease(rstop, "a")
onkeyrelease(rstop, "d")



while 1:
    tx, ty = t.pos()
    for laser in lasers:
        lasermove(laser)
        if laser.ycor() > TOP:
            laser.hideturtle()
            lasers.remove(laser)
            turtle.turtles().remove(laser)
        for enemy in enemies:
            if compare(enemy, laser) == 1:
                remove(enemy, enemies)
                remove(laser, lasers)
                score = score + 1
    if random.randint(1,rate) == 1:
        enema()
    for enemy in enemies:
        enemymove(enemy)
        if enemy.ycor() < BOTTOM:
            remove(enemy, enemies)
            lives = lives - 1
        if compare(enemy, t) == 1:
            lives = lives - 1
            remove(enemy, enemies)
    time_elapsed = time.time() - game_timer
    text.clear()
    text.write(
    f"Time: {time_elapsed:5.1f}s\nScore: {score:5}\nLives: {lives:5}\nAmmo: {ammo:5}",
    font=("Courier", 15, "bold"))
    new_x = t.xcor() + 3 * t.t_movement
    angle = 5 * t.t_rotation
    t.setheading(t.heading() + angle)
    if LEFT + GUTTER <= new_x <= RIGHT - GUTTER:
        t.setx(new_x)
        draw()
    if lives == 0:
        for enemy in enemies:
            remove(enemy, enemies)
        break
    if score % 10 == 0 and score > 0:
        espeed = espeed + 1
        rate = rate - 5
        ammo = ammo + 12

    window.update()

enemies.clear()
lasers.clear()

window.clear()
window.bgcolor('gray')
text.write(
f"Time: {time_elapsed:5.1f}s\nScore: {score:5}\nLives: {lives:5}\nAmmo: {ammo:5}",
font=("Courier", 15, "bold"))

text.goto(LEFT*.3,0)
text.write("GAME OVER", font=("Arial", 50, "bold"))


window.update()








turtle.done()
