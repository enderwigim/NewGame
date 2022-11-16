import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 1024, 768
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("My game")
FPS = 60

TILESIZE = 32
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE

PLAYER_WIDTH, PLAYER_HEIGHT = 32, 32