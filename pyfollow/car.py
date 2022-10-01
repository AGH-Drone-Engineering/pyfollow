import numpy as np
from pyfollow.world import WorldElement, Vector, Transform


class Sensor(WorldElement):
    def __init__(self, transform: Transform, parent: WorldElement):
        polygon = [
            Vector(-0.5, -1).mul(0.005),
            Vector(0.5, -1).mul(0.005),
            Vector(0.5, 1).mul(0.005),
            Vector(-0.5, 1).mul(0.005),
        ]
        super().__init__(polygon, transform, parent)


class SensorArray(WorldElement):
    def __init__(self, n, transform: Transform, parent: WorldElement):
        super().__init__([], transform, parent)
        width = n * 0.01
        self.sensors = [Sensor(Transform(Vector(x, 0), 0), self) for x in np.linspace(-width / 2, width / 2, n)]


class Wheel(WorldElement):
    def __init__(self, transform: Transform, parent: WorldElement):
        polygon = [
            Vector(-0.5, -1).mul(0.01),
            Vector(0.5, -1).mul(0.01),
            Vector(0.5, 1).mul(0.01),
            Vector(-0.5, 1).mul(0.01),
        ]
        super().__init__(polygon, transform, parent)


class Car(WorldElement):
    def __init__(self, transform: Transform, parent: WorldElement):
        super().__init__([], transform, parent)
        self.sensor_array = SensorArray(5, Transform(Vector(0, 0.07), 0), self)
        self.left_wheel = Wheel(Transform(Vector(-0.02, 0), 0), self)
        self.right_wheel = Wheel(Transform(Vector(0.02, 0), 0), self)
