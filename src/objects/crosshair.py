import pygame

from .game_object import GameObject


class Crosshair(GameObject):

    def __init__(self, x, y, width, height, crosshair_dir):
        super().__init__(x, y, width, height)
        self.__image = self.scale(self.load(str(crosshair_dir / 'crosshair.png')), width, height)

    def update(self):
        self._x = pygame.mouse.get_pos()[0] - self._width / 2
        self._y = pygame.mouse.get_pos()[1] - self._height / 2

    def draw(self, screen):
        screen.blit(self.__image, (self._x, self._y))
