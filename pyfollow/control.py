import numpy as np


class ControlSystem:
    def __init__(self, car):
        self._car = car

    def update(self, dt):
        sensors = [s.detection for s in self._car.sensor_array.sensors]
        sensors_left = sensors[:2]
        sensors_right = sensors[-2:]
        left = sum(1 for s in sensors_left if s)
        right = sum(1 for s in sensors_right if s)
        if left > right:
            self._car.set_motors(0, 0.3)
        elif right > left:
            self._car.set_motors(0.3, 0)
        else:
            self._car.set_motors(0.3, 0.3)

