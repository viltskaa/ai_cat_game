import pygame

import ai_logic


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load('assets/falling.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.__speed = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            ...

    def compute(self, scores):
        x, y = self.rect.center
        score_x, score_y = ai_logic.get_min_lenght_score(
            x, y, list(map(lambda x: x.rect.center, scores))
        )
        self.rect.center = ai_logic.move(x, y, score_x, score_y, self.__speed)
