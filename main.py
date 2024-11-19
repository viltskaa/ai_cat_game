import random

import pygame

import Sprites

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

sprites = pygame.sprite.Group()
scores_sprites = pygame.sprite.Group()

player = Sprites.Player(
    random.randrange(0, WIDTH),
    random.randrange(0, HEIGHT)
)
sprites.add(player)

scores = [
    Sprites.Score(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    for _ in range(10)
]

scores_sprites.add(*scores)
sprites.add(*scores)

lines = [(0, 0)]

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()
    player.compute(scores_sprites)

    if pygame.sprite.spritecollide(player, scores_sprites, True):
        score = Sprites.Score(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
        scores_sprites.add(score)
        sprites.add(score)

    screen.fill((128, 128, 128))
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
