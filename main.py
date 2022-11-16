import sprites
from engine import *
import pygame

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pygame.draw.line(WIN, BLACK, (0, y), (WIDTH, y))

def draw_window(character):
    WIN.fill(WHITE)
    character.draw(WIN)
    draw_grid()
    pygame.display.update()


def game():
    run = True
    clock = pygame.time.Clock()
    character = pygame.sprite.Group()

    new_character = sprites.Player(100, 200)
    character.add(new_character)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False


        key_pressed = pygame.key.get_pressed()
        character.update(key_pressed)
        draw_window(character)


if __name__ == "__main__":
    game()