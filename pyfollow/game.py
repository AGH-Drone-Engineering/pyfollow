import pygame
from pyfollow.world import World
from pyfollow.car import Car, Transform, Vector
from pyfollow.board import Board
from pyfollow.control import ControlSystem


class Game:
    def __init__(self):
        self._fps = 60
        self._clock = pygame.time.Clock()
        self._world = World()
        self._board = Board(Transform(Vector(0, 0), 0), self._world)
        self._car = Car(Transform(Vector(0, 0), 0), self._world)
        self._control_system = ControlSystem(self._car)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()

            self._control_system.update(1 / self._fps)
            self._car.update(1 / self._fps)

            screen.fill((0, 0, 0))
            self._world.draw(screen)
            pygame.display.flip()
            self._clock.tick(self._fps)
