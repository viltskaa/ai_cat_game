import random

import pygame

import Sprites
from Sprites import MapBlock
from Sprites.MapBlock import Air, Block
from Sprites.Player import can_move

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

sprites = pygame.sprite.Group()
scores_sprites = pygame.sprite.Group()
map_group = pygame.sprite.Group()

gamemap = [[0 for _ in range(WIDTH // MapBlock.WIDTH)] for _ in range(HEIGHT // MapBlock.HEIGHT)]


def create_map():
    for i in range(WIDTH // MapBlock.WIDTH):
        for j in range(HEIGHT // MapBlock.HEIGHT):
            is_wall = random.choice([True] * 25 + [False] * 1)
            block = Air(i * MapBlock.WIDTH, j * MapBlock.HEIGHT) if is_wall else Block(i * MapBlock.WIDTH,
                                                                                           j * MapBlock.HEIGHT)
            gamemap[i][j] = block
            map_group.add(block)


create_map()

player = Sprites.Player(
    random.randint(0, WIDTH),
    random.randint(0, HEIGHT)
)
while not can_move(player, map_group):
    player = Sprites.Player(
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT)
    )

sprites.add(player)

scores = [
    Sprites.Score(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    for _ in range(10)
]

scores_sprites.add(*scores)
sprites.add(*scores)

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.compute(scores_sprites, map_group)
    sprites.update()

    if pygame.sprite.spritecollide(player, scores_sprites, True):
        score = Sprites.Score(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        scores_sprites.add(score)
        sprites.add(score)

    screen.fill((128, 128, 128))
    map_group.draw(screen)
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
