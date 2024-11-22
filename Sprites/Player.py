import pygame

import ai_logic


def can_move(player, map_group):
    collide = pygame.sprite.spritecollide(player, map_group, False)
    if collide:
        for block in collide:
            if not block.air:
                return False
    return True


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('assets/falling.png'), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.__speed = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            ...

    def compute(self, scores, map_group):
        x, y = self.rect.center
        score_x, score_y = ai_logic.get_min_lenght_score(
            x, y, list(map(lambda x: x.rect.center, scores))
        )
        virtual_player = Player(*self.rect.topleft)
        virtual_player.rect.center = ai_logic.move(x, y, score_x, score_y, self.__speed)
        if can_move(virtual_player, map_group):
            self.rect.center = virtual_player.rect.center
