import tkinter as tk
from tkinter import *
from random import randrange
import math

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.x
    @x.setter
    def x(self,x):
        self.x = x
    @property
    def y(self):
        return self.y
    @y.setter
    def y(self,y):
        self.y = y
    def distance(self, other):
        i = (self.x - other.x) ** 2
        e = (self.y - other.y) ** 2
        d = math.sqrt((i+e))
        return float(d)
    def midpoint(self, other):
        i = (self.x + other.x)/2
        e = (self.y + other.y)/2
        return Point(i,e)
    def __string__(self):
        return "({:.1f}, {:.1f})".format(self.x,self.y)
        
class ChaosGame(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, background="white")
        self.pack(fill = BOTH, expand = 1)
    def plotPoints(self, b, n):
        x0, y0 = WIDTH/2, HEIGHT/2
        direction = (x0,y0)
        for i in range(n):
            point = randrange(len(base))
            direction = base[point]
            x0 = (direction[0] + x0) / 2
            y0 = (direction[1] + y0) / 2
            color = direction[1]
            self.plot(x0,y0)
    def plot(self,x,y):
        self.create_oval(x,y,x+POINT_RADIUS*2,y+POINT_RADIUS*2, outline = M_COLOR, fill = M_COLOR)
    def Vert(self):
        self.plotVert(MID_X, MIN_Y)
        self.plotVert(MAX_X, MAX_Y)
        self.plotVert(MIN_X,MAX_Y)
    def plotVert(self, x, y):
        self.create_oval(x,y,x + POINT_RADIUS*2,y+ POINT_RADIUS*2,outline = V_COLOR, fill = V_COLOR)
        
WIDTH = 600
HEIGHT = 520
V_COLOR = "black"
M_COLOR = "orange"
POINT_RADIUS = 3
NUM_POINTS = 50000
MIN_X = 4
MIN_Y = 4
MAX_X = 590
MAX_Y = 510
MID_X = (MIN_X + MAX_X) / 2
MID_Y = (MIN_Y + MAX_Y) / 2

V1 = (MID_X, MIN_Y)
V2 = (MAX_X, MAX_Y)
V3 = (MIN_X, MAX_Y)
base = (V1, V2, V3)
window = Tk()
window.title("Trianles")
window.geometry("{}x{}".format(WIDTH,HEIGHT))
r = ChaosGame(window)
r.plotPoints(base, NUM_POINTS)
r.Vert()
window.mainloop()

