import pygame
from pygame.locals import*

import sys

pygame.init()
screen_info = pygame.display.Info()

size = (width,height) = (screen_info.current_w,screen_info.current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255,224,179)
sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()
#print(screen_info)
#initial Setup with phase 1 complete
def main():
  game_over = False
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_f:
          pygame.display.set_mode(size,FULLSCREEN)
        if event.key == K_ESCAPE:
          pygame.display.set_mode(size)
  screen.fill(color)
  platforms.draw(screen)
  sprite_list.draw(screen)
  pygame.display.flip()

if __name__ == "__main__":
  main()


