import pygame
from sys import exit

pygame.init()

WIDTH = 1632
HEIGHT = 918

screen = pygame.display_set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Solver')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)
