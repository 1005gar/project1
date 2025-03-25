import pygame
import random
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабораторная работа 2. Упражнение 2")

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
          (255, 0, 255), (0, 255, 255), (255, 165, 0), (128, 0, 128)]


class Shape:
    def __init__(self, shape_type, x, y, width, height=None, color=None):
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.width = width
        self.height = height if height else width
        self.color = color if color else random.choice(COLORS)
        self.speed_x = random.randint(2, 5) * random.choice([-1, 1])
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.speed_x *= -1
            self.color = random.choice(COLORS)
        if self.y <= 0 or self.y + self.height >= HEIGHT:
            self.speed_y *= -1
            self.color = random.choice(COLORS)

    def draw(self):
        if self.shape_type == "square":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))
        elif self.shape_type == "rectangle":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.shape_type == "circle":
            pygame.draw.circle(screen, self.color, (int(self.x + self.width / 2), int(self.y + self.width / 2)),
                               self.width // 2)
        elif self.shape_type == "triangle":
            points = [
                (self.x + self.width // 2, self.y),
                (self.x, self.y + self.height),
                (self.x + self.width, self.y + self.height)
            ]
            pygame.draw.polygon(screen, self.color, points)

    def is_clicked(self, pos):
        if self.shape_type == "circle":
            distance = ((pos[0] - (self.x + self.width / 2)) ** 2 + (pos[1] - (self.y + self.width / 2)) ** 2) ** 0.5
            return distance <= self.width / 2
        else:
            return (self.x <= pos[0] <= self.x + self.width and
                    self.y <= pos[1] <= self.y + (
                        self.height if self.shape_type in ["rectangle", "triangle"] else self.width))


shapes = [
    Shape("square", 100, 100, 50),
    Shape("rectangle", 200, 200, 80, 40),
    Shape("circle", 300, 300, 60),
    Shape("triangle", 400, 400, 70, 70)
]

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for shape in shapes:
                    if shape.is_clicked(event.pos):
                        shape.color = random.choice(COLORS)

    for shape in shapes:
        shape.move()
        shape.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()