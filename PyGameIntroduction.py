import pygame
import random

pygame.init()

font1 = pygame.font.Font("freesansbold.ttf", 20)
WIDTH,HEIGHT = 900,600
pygame.display.set_caption("pong")
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
FPS = 30

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

class Striker():
  def __init__(self,xpos,ypos,width,height,speed,color):
    self.xpos = xpos
    self.ypos = ypos
    self.width = width
    self.height = height
    self.speed = speed
    self.color = color

    self.geekRect = pygame.Rect(xpos,ypos,width,height)
    self.geek = pygame.draw.rect(screen,self.color,self.geekRect)
  
  def display(self):
    self.geek = pygame.draw.rect(screen,self.color,self.geekRect)

  def displayScore(self,text,score,x,y,color):
    text = font1.render(text+str(score),True,color)
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(text,textRect)

  def update(self, yFac):
    self.ypos = self.ypos + self.speed *yFac

    if self.ypos <= 0:
      self.ypos = 0
    elif self.ypos + self.height >= HEIGHT:
      self.ypos = HEIGHT - self.height

    self.geekRect = (self.xpos,self.ypos,self.width,self.height)

  def getRect(self):
    return self.geekRect 

class Ball():
  def __init__(self,xpos,ypos,radius,speed,color):
    self.xpos = xpos
    self.ypos = ypos
    self.radius = radius
    self.speed = speed
    self.color = color
    self.xFac = 1
    self.yFac = -1
    self.ball = pygame.draw.circle(screen,self.color,(self.xpos,self.ypos),self.radius)

    self.firstTime = 1
  def display(self):
    self.ball = pygame.draw.circle(screen,self.color,(self.xpos,self.ypos),self.radius)

  def update(self):
    self.xpos += self.speed * self.xFac
    self.ypos += self.speed * self.yFac

    if self.ypos <= 0 or self.ypos >= HEIGHT:
      self.yFac *= -1
    if self.xpos <= 0 and self.firstTime:
      self.firstTime = 0
      return 1
    elif self.xpos >= WIDTH and self.firstTime:
      self.firstTime = 0
      return -1
    else:
      return 0

  def reset(self):
    self.xpos = WIDTH // 2
    self.ypos = HEIGHT // 2
    self.xFac *= -1
    self.firstTime = 1
    self.speed = 10

  def hit(self):
    self.xFac *= -1
    self.speed += 5

  def getRect(self):
    return self.ball

def main():
  running = True
  geek1 = Striker(20,0,10,100,20,GREEN)
  geek2 = Striker(WIDTH-30,0,10,100,20,GREEN)
  ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)
  
  listofgeeks = [geek1, geek2]

  geek1score, geek2score = 0,0
  geek1YFac, geek2YFac = 0,0

  while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          geek2YFac = -1
        if event.key == pygame.K_DOWN:
          geek2YFac = 1
        if event.key == pygame.K_w:
          geek1YFac = -1
        if event.key == pygame.K_s:
          geek1YFac = 1
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          geek2YFac = 0
        if event.key == pygame.K_w or event.key == pygame.K_s:
          geek1YFac = 0
    for geek in listofgeeks:
      if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
        ball.hit()

    geek1.update(geek1YFac)
    geek2.update(geek2YFac)
    point = ball.update()

    if point == -1:
      geek1score += 1
    elif point == 1:
      geek2score += 1
    
    if point:
      ball.reset()

    geek1.display()
    geek2.display()
    ball.display()
    
    geek1.displayScore("Player 1: ",geek1score,100,20,WHITE)
    geek2.displayScore("Player 2: ", geek2score,WIDTH-100,20,WHITE)

    
    pygame.display.update()
    clock.tick(FPS)
      
if __name__ == "__main__":
  main()
  pygame.quit()