from math import sqrt

from game import settings
from game.entities.entity import Entity


class Slime(Entity):

    def __init__(self, x, y, width, height, speed=3):
        super().__init__(x, y, width, height)
        self.__slime_res = settings.slime_res
        self.__speed = speed
        self.__dx = 0
        self.__dy = 0
        self.__vx = 0
        self.__vy = 0

        self.__move_anim = [
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f0.png')), width, height),
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f1.png')), width, height),
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f2.png')), width, height),
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f3.png')), width, height),
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f4.png')), width, height),
            self.scale(self.load(str(self.__slime_res / 'slime_run_anim_f5.png')), width, height)
        ]

        self.__anim = self.__move_anim
        self.__frame = 0
        self.__image = self.__anim[int(self.__frame)]
        self.__image.get_rect()

    def draw(self, screen):
        screen.blit(self.__image, (self._x, self._y))

    def update(self, dt):
        self.__frame += 0.2
        if self.__frame >= len(self.__anim):
            self.__frame = 0
        self.__image = self.__anim[int(self.__frame)]

    def move(self, dx, dy):
        self.__vx = dx * self.__speed
        self.__vy = dy * self.__speed
        self._x += self.__vx
        self._y += self.__vy

    def move_to_player(self, player_center):
        self_pos = self.get_center()
        dir_x = self_pos[0] - player_center[0]
        dir_y = self_pos[1] - player_center[1]
        dir_len = sqrt(pow(dir_x, 2) + pow(dir_y, 2))
        dir_x = dir_x / dir_len
        dir_y = dir_y / dir_len
        self.move(-dir_x, -dir_y)
