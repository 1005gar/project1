import pygame
import time

pygame.init()

window_width = 800
window_height = 600
fon = 'fon.png'
hero_img = 'valorant.png'

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Игра v1.0")

img1 = pygame.image.load(fon)
back_fon = pygame.transform.scale(img1, (window_width, window_height))
sdvig_fona = 0
bg_speed = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, hero_x=100, hero_y=250, x_speed=0, y_speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)  # загрузка героя из файла
        self.rect = self.image.get_rect()
        self.hero_x = hero_x
        self.hero_y = hero_y
        # стартовые позиции персонажа:
        self.rect.x = hero_x
        self.rect.y = hero_y
        # скорость движения спрайта:
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        """Перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость"""
        global bg_speed

        self.rect.x += self.x_speed

        if self.rect.right > window_width - 50 and self.x_speed > 0:
            bg_speed = -self.x_speed
            self.rect.x = window_width - 50
        elif self.rect.left < 50 and self.x_speed < 0:
            bg_speed = -self.x_speed
            self.rect.x = 50
        else:
            bg_speed = 0

        self.rect.y += self.y_speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height:
            self.rect.bottom = window_height


hero = Player(hero_img)
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                hero.x_speed = 5
            elif event.key == pygame.K_UP:
                hero.y_speed = -5
            elif event.key == pygame.K_DOWN:
                hero.y_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                hero.x_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                hero.y_speed = 0

    hero.update()

    sdvig_fona = (sdvig_fona + bg_speed) % window_width

    window.blit(back_fon, (sdvig_fona, 0))
    if sdvig_fona != 0:
        window.blit(back_fon, (sdvig_fona - window_width, 0))
    elif bg_speed < 0:
        window.blit(back_fon, (sdvig_fona + window_width, 0))

    all_sprites.draw(window)

    pygame.display.update()
    time.sleep(0.02)

pygame.quit()