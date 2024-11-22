import pygame.sprite


class MapBlock(pygame.sprite.Sprite):
    WIDTH = 5
    HEIGHT = 5

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.surface.Surface((
            MapBlock.WIDTH,
            MapBlock.HEIGHT
        ))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Air(MapBlock):
    def __init__(self, x: int, y: int):
        MapBlock.__init__(self, x, y)
        self.air = True


class Block(MapBlock):
    def __init__(self, x: int, y: int):
        MapBlock.__init__(self, x, y)
        self.air = False
        self.image.fill((78, 78, 78))
