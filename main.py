import pygame,sys,time,pymunk
import random
def create_Apple(Space,pos):
  global count
  body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
  body.position = pos
  shape = pymunk.Circle(body,20)
  Space.add(body,shape)
  return shape
def drawApples(apples):
  global height,width
  global x,y,xAdd,yAdd
  if apples!=[]:
    x-=xAdd
    y+=yAdd
      
  for apple in apples:
    POS_X = int(apple.body.position.x)
    POS_Y = int(apple.body.position.y)
    apple_rect = appleIMG.get_rect(center=(POS_X,POS_Y))
    if outOfBounds(POS_X,POS_Y,height,width):
      
      xAdd= -1*xAdd
      yAdd= -1*yAdd
    screen.blit(appleIMG,apple_rect)
xAdd = .018
yAdd = .01    
def static_object(Space,posX,posY):
  body = pymunk.Body(body_type= pymunk.Body.STATIC)
  body.position = (posX,posY) 
  shape = pymunk.Circle(body,15)
  Space.add(body,shape) 
  return shape
def static (objects):
  for object in objects:
    POS_X = int(object.body.position.x)
    POS_Y = int(object.body.position.y)
    pygame.draw.circle(screen,(0,60,0),(POS_X,POS_Y),15)

width = 600
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
Space = pymunk.Space()
Space.gravity = (0,100)
appleIMG = pygame.image.load("apple.png")
apples = []
objects = []
objects.append(static_object(Space,100,200))
firsttime = 0
fps = ""
apples.append(create_Apple(Space,(50,50)))
def outOfBounds(x,y,width,height):
  if x <0 or x > width or y < 0 or y > height:
    return True
  else:
    return False
x=4
y = 1
a=0
while True:
  firsttime = time.time()
  Space.gravity = (x,y)
  screen.fill((217,217,217))
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      apples.append(create_Apple(Space,event.pos))
  if apples !=[] and a == 0:
    a = 1
    x,y=4,1
    drawApples(apples)
  elif apples!=[]:
    drawApples(apples)
  else:
    a = 0
  static(objects)
  print(x,y)
  pygame.display.update()
  Space.step(1/50)
  fps = str((int((1/(time.time()-firsttime)))))
  #print ("FPS: "+ fps)
  #print(len(apples))

