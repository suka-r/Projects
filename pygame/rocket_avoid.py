

import pygame
import random
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_SPACE, KEYDOWN, K_q, QUIT)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("./img/jet.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.move_up_sound = pygame.mixer.Sound("./audio/Rising_putter.ogg")
        self.move_down_sound = pygame.mixer.Sound("./audio/Falling_putter.ogg")
        self.move_up_sound.set_volume(0.2) 
        self.move_down_sound.set_volume(0.2)

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            self.move_up_sound.play()
        elif keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            self.move_down_sound.play()
        elif keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        elif keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("./img/missile.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT) #diff positsions
        self.speed = random.randint(5, 20)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('./img/cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL) # black will be transparent 
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT)  
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        super().__init__()
        self.xy = 160
        self.num_frames = 12
        self.image = pygame.image.load('./img/explosion_frames.png')
        self.image = pygame.transform.scale(self.image, (12 * self.xy, self.xy))
        self.current_frame = 0
        self.frames = []
        for i in range(self.num_frames):
            frame = self.image.subsurface(pygame.Rect(i * self.xy, 0, self.xy, self.xy))
            self.frames.append(frame)

        self.surf = self.frames[self.current_frame]
        self.rect = player_pos

    def update(self):
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[self.current_frame]




class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        self.player = Player()

        self.enemies_group = pygame.sprite.Group()
        self.explosions_group = pygame.sprite.Group()

        self.clouds_group = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        pygame.mixer.music.load('./audio/Apoxode_-_Electric_1.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        self.running = True
        
    def setup(self):
        if random.randint(0, 50) < 10:
            self.enemies_group.add(Enemy())

        if random.randint(0, 50) < 2:
            self.clouds_group.add(Cloud())
        self.all_sprites.add(self.clouds_group, self.enemies_group)

    def play_game(self):
        while self.running :
            for event in pygame.event.get():
                if event.type == QUIT:
                    QUIT

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        QUIT

            self.setup()
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.draw_screen()
            if pygame.sprite.spritecollideany(self.player,  self.enemies_group):
                self.crash()

            
            pygame.display.flip()
            self.clock.tick(30)

    def draw_screen(self):
        self.screen.fill((135, 206, 250))
        self.clouds_group.update() 
        self.enemies_group.update()
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
    
    def crash(self):
        pygame.mixer.music.stop()
        expl_loc = self.player.rect
        explosion = Explosion(expl_loc)
        self.all_sprites.add(explosion)
        self.player.kill()
        pygame.mixer.music.load('./audio/explosion.mp3')
        pygame.mixer.music.play(1)
        
        for each in explosion.frames:
            self.draw_screen()
            explosion.update()
            pygame.display.flip()
            self.clock.tick(30)
        
        self.replay_screen()


    def replay_screen(self):
        font1 = pygame.font.SysFont("Grobold", 50)
        text_surface = font1.render("Press SPACE to Continue or ESC to Exit", True, pygame.Color(255, 255, 255))
        self.screen.blit(text_surface, ((SCREEN_WIDTH / 2) - (text_surface.get_width() / 2), SCREEN_HEIGHT * 7 / 8))
        pygame.display.flip()

        x = True
        while x:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        x = False
                        self.enemies_group.empty()
                        self.clouds_group.empty()
                        self.all_sprites.empty()
                        self.all_sprites.add(self.player)
                        self.running = True
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        x = False

        pygame.display.flip()
        self.clock.tick(30)


if __name__ == "__main__":
    game = Game()
    game.play_game()



