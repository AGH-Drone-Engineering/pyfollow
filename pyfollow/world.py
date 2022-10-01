from typing import NamedTuple
import math
import pygame


class Vector(NamedTuple):
    x: float
    y: float

    def rotate(self, angle: float) -> 'Vector':
        return Vector(
            x=self.x * math.cos(angle) - self.y * math.sin(angle),
            y=self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def add(self, other: 'Vector') -> 'Vector':
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def mul(self, scalar: float) -> 'Vector':
        return Vector(
            x=self.x * scalar,
            y=self.y * scalar,
        )


class Transform(NamedTuple):
    translation: Vector
    rotation: float

    def add(self, other: 'Transform') -> 'Transform':
        return Transform(
            translation=self.transform(other.translation),
            rotation=self.rotation + other.rotation,
        )

    def transform(self, vector: Vector) -> Vector:
        return vector.rotate(self.rotation).add(self.translation)


class WorldElement:
    def __init__(self, polygon: list[Vector], transform: Transform, parent: 'WorldElement'):
        self._polygon = polygon
        self._transform = transform
        self._parent = parent
        self._world: World = parent._world
        self._world.add_element(self)

    @property
    def global_transform(self) -> Transform:
        return self._parent.global_transform.add(self._transform)

    @property
    def global_polygon(self) -> list[Vector]:
        return [self.global_transform.transform(point) for point in self._polygon]


class World:
    def __init__(self):
        self._elements: list[WorldElement] = []
        self._world = self

    @property
    def global_transform(self) -> Transform:
        return Transform(Vector(0, 0), 0)

    def draw(self, screen: pygame.Surface):
        screen_x_min = screen.get_width() * 0.1
        screen_x_max = screen.get_width() * 0.9
        screen_y_min = screen.get_height() * 0.1
        screen_y_max = screen.get_height() * 0.9
        x_min = 0
        y_min = 0
        x_max = 0
        y_max = 0

        for element in self._elements:
            for point in element.global_polygon:
                x_min = min(x_min, point.x)
                y_min = min(y_min, point.y)
                x_max = max(x_max, point.x)
                y_max = max(y_max, point.y)

        screen_aspect = (screen_x_max - screen_x_min) / (screen_y_max - screen_y_min)
        world_aspect = (x_max - x_min) / (y_max - y_min)
        if screen_aspect > world_aspect:
            scale = (screen_y_max - screen_y_min) / (y_max - y_min)
        else:
            scale = (screen_x_max - screen_x_min) / (x_max - x_min)

        for element in self._elements:
            polygon = []
            for point in element.global_polygon:
                polygon.append((
                    screen_x_min + (point.x - x_min) * scale,
                    screen_y_max - (point.y - y_min) * scale,
                ))
            if len(polygon) > 0:
                pygame.draw.polygon(screen, (255, 255, 255), polygon, 1)

    def add_element(self, element: WorldElement):
        self._elements.append(element)
