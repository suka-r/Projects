

# import pygame
# import random


# class Explosion(pygame.sprite.Sprite):
#         def __init__(self):
#             super().__init__()
                 
#             self.xy = 160
#             num_frames = 12
                 
#             sprite_sheet = pygame.image.load('./img/explosion_frames.png')    
#             sprite_sheet = pygame.transform.scale(sprite_sheet, (num_frames*self.xy, self.xy))
         
#             self.current_frame = 0
#             self.frames = []
         
                 
#             for i in range(num_frames):
#                 frame = sprite_sheet.subsurface(pygame.Rect(i * self.xy, 0, self.xy, self.xy))
#                 self.frames.append(frame)
#                 self.surf = self.frames[self.current_frame]
#                 self.rect = self.surf.get_rect()


#         def update(self):
#             self.current_frame += 1
#             if self.current_frame >= len(self.frames):
#                 self.kill()  
#             else:
#                 self.surf = self.frames[self.current_frame]


# class Game:
#     def __init__(self):
#         self.screen = None
#         self.clock = pygame.time.Clock()
#         self.red = 0, 0, 25
#         self.blue = 0, 191, 255
#         self.player = None
#         #Create groups to hold enemy sprites, cloud sprites, and all sprites
#         self.enemies = pygame.sprite.Group()
#         self.clouds = pygame.sprite.Group()
       
#         self.collision_sound = None
#         self.explosion_sound = None
   


#     def setup(self):
#         pygame.init()
#         pygame.mixer.init()


#         self.screen = pygame.display.set_mode((800, 600))
#         # self.screen.fill((135, 206, 250))


#         player_image = pygame.image.load("./img/jet.png").convert()
#         enemy_image = pygame.image.load("./img/missile.png").convert()
#         clouds_image = pygame.image.load("./img/cloud.png").convert()


#         for _ in range(5):  #5 clouds 5 enemies
#             cloud = pygame.sprite.Sprite()
#             enemy = pygame.sprite.Sprite()
   
#             cloud.rect = clouds_image.image.get_rect()
#             enemy.rect = enemy_image.image.get_rect()


#             cloud.rect.x = random.randrange(0, 800)
#             cloud.rect.y = random.randrange(0, 200)
           
#             enemy.rect.x = random.randrange(0, 800)
#             enemy.rect.y = random.randrange(0, 600)


#             self.enemies.add(enemy)
#             self.clouds.add(cloud)


#         pygame.mixer.music.load("./audio/Apoxode_-_Electric_1.mp3")
#         pygame.mixer.music.play(loops=-1)
#         self.collision_sound = pygame.mixer.Sound("./audio/Collision.ogg")
#         self.explosion_sound = pygame.mixer.Sound("./audio/explosion.ogg")


#         self.collision_sound.set_volume(0.5)
#         self.explosion_sound.set_volume(0.5)


#     def draw_screen(self):
#         self.screen.fill((135, 206, 250))


#         # Draw all our sprites
#         for entity in self.all_sprites:
#             self.screen.blit(entity.surf, entity.rect)


#     def play_game(self):
#         pass
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False


#                 else:
#                     pass
#                     # if event.type == pygame.KEYDOWN:
#                     #     keys = pygame.key.get_pressed()
#                     # if keys[pygame.K_UP]:
#                     #     rect1.y -= 10
#                     # elif keys[pygame.K_DOWN]:
#                     #      rect1.y += 10
#                     # elif keys[pygame.K_RIGHT]:
#                     #     rect1.x += 10
#                     # elif keys[pygame.K_LEFT]:
#                     #     rect1.x -= 10



# class Player:
#     def __init__(self):
#         super().__init__()
#         self.move_up_sound = pygame.mixer.Sound("./audio/Rising_putter.ogg")
#         self.move_down_sound = pygame.mixer.Sound("./audio/Falling_putter.ogg")
#         self.volume = 0.5












# import pygame
# import random


# class Explosion(pygame.sprite.Sprite):
#         def __init__(self):
#             super().__init__()
                 
#             self.xy = 160
#             num_frames = 12
                 
#             sprite_sheet = pygame.image.load('./img/explosion_frames.png')    
#             sprite_sheet = pygame.transform.scale(sprite_sheet, (num_frames*self.xy, self.xy))
         
#             self.current_frame = 0
#             self.frames = []
         
                 
#             for i in range(num_frames):
#                 frame = sprite_sheet.subsurface(pygame.Rect(i * self.xy, 0, self.xy, self.xy))
#                 self.frames.append(frame)
#                 self.surf = self.frames[self.current_frame]
#                 self.rect = self.surf.get_rect()


#         def update(self):
#             self.current_frame += 1
#             if self.current_frame >= len(self.frames):
#                 self.kill()  
#             else:
#                 self.surf = self.frames[self.current_frame]


# class Game:
#     def __init__(self):
#         self.screen = None
#         self.clock = pygame.time.Clock()
#         self.red = 0, 0, 25
#         self.blue = 0, 191, 255
#         self.player = None
#         #Create groups to hold enemy sprites, cloud sprites, and all sprites
#         self.enemies = pygame.sprite.Group()
#         self.clouds = pygame.sprite.Group()
       
#         self.collision_sound = None
#         self.explosion_sound = None
   


#     def setup(self):
#         pygame.init()
#         pygame.mixer.init()


#         self.screen = pygame.display.set_mode((800, 600))
#         # self.screen.fill((135, 206, 250))


#         player_image = pygame.image.load("./img/jet.png").convert()
#         enemy_image = pygame.image.load("./img/missile.png").convert()
#         clouds_image = pygame.image.load("./img/cloud.png").convert()


#         for _ in range(5):  #5 clouds 5 enemies
#             cloud = pygame.sprite.Sprite()
#             enemy = pygame.sprite.Sprite()
   
#             cloud.rect = clouds_image.image.get_rect()
#             enemy.rect = enemy_image.image.get_rect()


#             cloud.rect.x = random.randrange(0, 800)
#             cloud.rect.y = random.randrange(0, 200)
           
#             enemy.rect.x = random.randrange(0, 800)
#             enemy.rect.y = random.randrange(0, 600)


#             self.enemies.add(enemy)
#             self.clouds.add(cloud)


#         pygame.mixer.music.load("./audio/Apoxode_-_Electric_1.mp3")
#         pygame.mixer.music.play(loops=-1)
#         self.collision_sound = pygame.mixer.Sound("./audio/Collision.ogg")
#         self.explosion_sound = pygame.mixer.Sound("./audio/explosion.ogg")


#         self.collision_sound.set_volume(0.5)
#         self.explosion_sound.set_volume(0.5)


#     def draw_screen(self):
#         self.screen.fill((135, 206, 250))


#         # Draw all our sprites
#         for entity in self.all_sprites:
#             self.screen.blit(entity.surf, entity.rect)


   


                # else:
                #     pass
                #     # if event.type == pygame.KEYDOWN:
                #     #     keys = pygame.key.get_pressed()
                #     # if keys[pygame.K_UP]:
                #     #     rect1.y -= 10
                #     # elif keys[pygame.K_DOWN]:
                #     #      rect1.y += 10
                #     # elif keys[pygame.K_RIGHT]:
                #     #     rect1.x += 10
                #     # elif keys[pygame.K_LEFT]:
                #     #     rect1.x -= 10


# class Player:
#     def __init__(self):
#         super().__init__()
#         self.move_up_sound = pygame.mixer.Sound("./audio/Rising_putter.ogg")
#         self.move_down_sound = pygame.mixer.Sound("./audio/Falling_putter.ogg")
#         self.volume = 0.5

        



# def play_game(self):
#     pass
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False



from typing import Any
import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./img/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 5

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        elif keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        elif keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        elif keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemies, self).__init__()
        self.surf = pygame.image.load("./img/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = SCREEN_WIDTH  # Start enemies from the right side
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed =  random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)  # Move enemies from right to left

        if self.rect.right < 0:  # Reset the position if the enemy goes off the left side
            self.rect.x = SCREEN_WIDTH
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            self.speed = random.randint(2, 5)  # Randomize speed again

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player = Player()

# Creating a sprite group for enemies
enemies_group = pygame.sprite.Group()

# Adding multiple enemy instances to the sprite group
for _ in range(10):  # Increase the number of enemies
    enemies_group.add(Enemies())

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update all the enemies in the sprite group
    enemies_group.update()

    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)

    # Draw all the enemies in the sprite group
    for enemy in enemies_group:
        screen.blit(enemy.surf, enemy.rect)

        

    pygame.display.flip()
    clock.tick(30)
