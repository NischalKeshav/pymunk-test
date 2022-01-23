import pygame,sys, pymunk 


def create_Apple(Space):
  body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
  body.position = (400,0)
  shape = pymunk.Circle(body,80)
  Space.add(body,shape)
  return shape
def drawApples(apples):
  for apple in apples:
    POS_X = int(apple.body.position.x)
    POS_Y = int(apple.body.position.y)
    pygame.draw.circle(screen,(0,0,0),(POS_X,POS_Y),80)
    print(POS_X)
    print (POS_Y)
def
    
pygame.init() #initialize pygame
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
Space = pymunk.Space()
Space.gravity = (40,150)

apples = []
apples.append(create_Apple(Space))
while True:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.fill((217,217,217))
  drawApples(apples)
    
  pygame.display.update()
  Space.step(1/50)
  clock.tick(120)