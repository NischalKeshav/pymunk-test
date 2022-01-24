import pygame,sys, pymunk ,random


def create_Apple(Space,pos):
  body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
  body.position = pos
  shape = pymunk.Circle(body,20)
  Space.add(body,shape)
  return shape
def drawApples(apples):
  for apple in apples:
    POS_X = int(apple.body.position.x)
    POS_Y = int(apple.body.position.y)
    apple_rect = appleIMG.get_rect(center=(POS_X,POS_Y))
    screen.blit(appleIMG,apple_rect)
    print(POS_X)
    print (POS_Y)
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

pygame.init() #initialize pygame
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
Space = pymunk.Space()
Space.gravity = (0,50)
appleIMG = pygame.image.load("apple.png")
apples = []
objects = []
objects.append(static_object(Space,100,200))
while True:
  apples.append(create_Apple(Space,((40+random.randrange(0,50)),40)))
  apples.append(create_Apple(Space,((40+random.randrange(0,50)),60)))
  apples.append(create_Apple(Space,((40+random.randrange(0,50)),90)))
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      apples.append(create_Apple(Space,event.pos))
  screen.fill((217,217,217))
  drawApples(apples)
  static(objects)
  pygame.display.update()
  Space.step(1/50)
