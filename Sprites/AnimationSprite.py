import pygame


class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.__ticks = 0
        self.__current_animation = None
        self.__start_animation_tick = None
        self.__last_index = None
        self.__images = {}
        self.load_images(images)

    def get_normal_image(self):
        return self.__images['normal'][0][0]

    def load_images(self, images):
        for key in images.keys():
            paths_images, delay = images[key]

            pygame_images = []
            for path in paths_images:
                img = pygame.image.load(path)
                img = pygame.transform.scale(img, (64, 64))
                pygame_images.append(img)

            self.__images.update({
                key: (pygame_images, delay)
            })

        self.image = self.__images["normal"][0][0]

    def run_animation(self, key: str):
        if key in self.__images:
            self.__current_animation = key

    def process_animation(self):
        self.__ticks += 1

        if self.__current_animation is None:
            return

        if self.__start_animation_tick is None:
            self.__start_animation_tick = self.__ticks

        animation_images, delay = self.__images[self.__current_animation]

        if self.__ticks - self.__start_animation_tick >= len(animation_images) * delay:
            self.__current_animation = None
            self.__start_animation_tick = None
            self.image = self.__images["normal"][0][0]
            return

        index = (self.__ticks - self.__start_animation_tick) // delay
        if index < len(animation_images) - 1 and self.__last_index != index:
            self.__last_index = index
            self.image = animation_images[index]