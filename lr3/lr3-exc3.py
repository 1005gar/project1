import pygame
import sys
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Битва")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

try:
    background = pygame.image.load('fon.png')
    background = pygame.transform.scale(background, (window_width, window_height))
    hero_img = pygame.image.load('hero.png')
    enemy_img = pygame.image.load('enemy.png')
    arrow_img = pygame.image.load('arrow.png')
except:
    background = pygame.Surface((window_width, window_height))
    background.fill((100, 100, 255))
    hero_img = pygame.Surface((50, 50))
    hero_img.fill((255, 0, 0))
    enemy_img = pygame.Surface((40, 40))
    enemy_img.fill((0, 255, 0))
    arrow_img = pygame.Surface((20, 5))
    arrow_img.fill((255, 255, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = hero_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, window_height // 2)
        self.speed = 5
        self.arrows = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.x = max(0, min(self.rect.x, window_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, window_height - self.rect.height))

    def shoot(self):
        arrow = Arrow(self.rect.right, self.rect.centery)
        self.arrows.add(arrow)
        all_sprites.add(arrow)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(window_width, window_width + 100)
        self.rect.y = random.randrange(0, window_height - self.rect.height)
        self.speed = random.randrange(1, 4)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randrange(window_width, window_width + 100)
            self.rect.y = random.randrange(0, window_height - self.rect.height)
            self.speed = random.randrange(1, 4)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = arrow_img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > window_width:
            self.kill()


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(enemies, player.arrows, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    window.blit(background, (0, 0))
    all_sprites.draw(window)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()