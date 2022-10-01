import pygame
from pyfollow.world import World
from pyfollow.car import Car, Transform, Vector
from pyfollow.board import Board


class Game:
    def __init__(self):
        self._fps = 30
        self._clock = pygame.time.Clock()
        self._world = World()
        Car(Transform(Vector(0, 0), 0.2), self._world)
        Board(Transform(Vector(0, 0), 0), self._world)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()

            screen.fill((0, 0, 0))
            self._world.draw(screen)
            pygame.display.flip()
            self._clock.tick(self._fps)
