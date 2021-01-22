import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, images):
        super().__init__()
        self.images = images
        self.image = images['p1_jump']
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # index 0 represents dx, index 1 represents dy
        self.xy_speed = pygame.math.Vector2(0, 0)
        self.facing = "R"
        self.jump_speed = -14

    def update(self, platforms):
        screen_info = pygame.display.Info()
        #update the image and direction
        self.image = self.images['p1_jump']
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True,False)
        
        # move the player
        self.rect.move_ip(self.xy_speed)
        # handle left/right movement
        self.xy_speed[0] = 0
        if self.rect.right < 0:
          self.rect.left = screen_info.current_w
        elif self.rect.left > screen_info.current_w:
          self.rect.right = 0   
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for plat in hit_list:
          if self.xy_speed[1] > 0 and abs(self.rect.bottom -plat.rect.top <= self.xy_speed[1]):
            self.rect.bottom = plat.rect.top
            self.xy_speed[1] = self.jump_speed


    def left(self):
        self.facing = 'L'
        self.xy_speed[0] = -6

    def right(self):
        self.facing = 'R'
        self.xy_speed[0] = 6