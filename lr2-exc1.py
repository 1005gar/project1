import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill([255, 255, 255])
pygame.display.set_caption('Лабораторная 2. Упражнение 1')

pygame.draw.circle(screen, 'red', [200, 100], 30, width=0)
pygame.draw.circle(screen, [255, 154, 13], [100, 400], 50, width=15)
pygame.draw.circle(screen, '#FFEE54', [400, 300], 100, width=5)

pygame.draw.rect(screen, 'yellow', [400, 20, 300, 200], 0)

for i in range(5):
    top = random.randint(50, 700)
    left = random.randint(50, 500)
    w = random.randint(10, 200)
    h = random.randint(10, 100)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pygame.draw.rect(screen, color, [top, left, w, h], 4)

dots = [[221, 432], [262, 331], [133, 342], [141, 310],
        [51, 230], [74, 217], [56, 153], [114, 164],
        [123, 135], [176, 190], [159, 77], [193, 93],
        [230, 261], [267, 93], [301, 77], [284, 190],
        [327, 135], [336, 164], [402, 153], [386, 217],
        [409, 230], [319, 310], [327, 342], [233, 331],
        [237, 432]]
pygame.draw.lines(screen, 'green', True, dots, 2)

# Домик с крышей по центру экрана
center_x, center_y = 400, 300  # Центр экрана 800x600
house_width = 200
house_height = 150
roof_height = 100

pygame.draw.rect(screen, 'brown',
                [center_x - house_width//2, center_y - house_height//2,
                 house_width, house_height], 0)

roof_points = [
    [center_x, center_y - house_height//2 - roof_height],
    [center_x - house_width//2, center_y - house_height//2],
    [center_x + house_width//2, center_y - house_height//2]
]
pygame.draw.polygon(screen, 'red', roof_points, 0)

door_width = 40
door_height = 80
pygame.draw.rect(screen, 'black',
                [center_x - door_width//2, center_y + house_height//2 - door_height,
                 door_width, door_height], 0)

window_size = 40
pygame.draw.rect(screen, 'blue',
                [center_x - house_width//4 - window_size//2, center_y - house_height//4,
                 window_size, window_size], 0)
pygame.draw.rect(screen, 'blue',
                [center_x + house_width//4 - window_size//2, center_y - house_height//4,
                 window_size, window_size], 0)

try:
    apple = pygame.image.load('apple.png')
    screen.blit(apple, [500, 300])
except:
    pass

pygame.display.flip()

pygame.time.delay(2000)
pygame.draw.rect(screen, 'white', [400, 450, 100, 100], 0)
try:
    screen.blit(apple, [600, 450])
except:
    pass

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()