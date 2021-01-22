import pygame, random 

class Platforms(pygame.sprite.Sprite):
  def __init__(self,pos,img_path,width=70,height=70):
    super().__init__()
    #.covert creates new copy of the surface with the pixel format changed
    self.image = pygame.Surface([width,height]).convert()
    self.image.blit(pygame.image.load(img_path).convert(),(0,0),(0,0,width,height))
    self.rect = self.image.get_rect()
    self.rect.center = pos
  
  def scroll(self,change):
    self.rect.top += change


