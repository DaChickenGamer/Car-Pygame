import pygame, sys
from pygame.locals import QUIT
pygame.init()
x_pos=400 
y_pos=400
x=2000
y=2000
screen = pygame.display.set_mode((x,y))
class PlayerCar(pygame.sprite.Sprite):
  def __init__(self,car_image,x_pos,y_pos):
    self.car_image=car_image
    self.x_pos=x_pos
    self.y_pos=y_pos
  def draw (self,screen):
    screen.blit(self.car_image,(self.x_pos,self.y_pos))
  def move_left(self):
    self.x_pos-=5
  def move_right(self):
    self.x_pos+=5
pygame.display.set_caption('start game!')
car_texture=pygame.image.load("images (5).jpeg")
backround=pygame.image.load("download (5).jpeg")
backround=pygame.transform.scale(backround,(900,900))
screen.blit(backround,(0,0))
car_surface=pygame.Surface((car_texture.get_width(),car_texture.get_height()))
car_surface.blit(car_texture,(0,0))
player_car=PlayerCar(car_surface,x_pos, y_pos)
player_car.draw(screen)
running=True
while running :
    for event in pygame.event.get():  
        if event.type == QUIT:
          running=False
        elif event.type==pygame.KEYDOWN:
          if event.type==pygame.K_LEFT:
            player_car.move_left()
          if event.type==pygame.K_RIGHT:
            player_car.move_right()
    screen.fill((0,0,0))
    player_car.draw(screen)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
sys.exit()
