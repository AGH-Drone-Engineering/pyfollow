import numpy as np
from pyfollow.pid import PID


class ControlSystem:
    def __init__(self, car):
        self._car = car
        self._pid = PID(0.07, 0.015)
        self._last_error = 0

    def get_line_position(self):
        return np.mean([i for i, s in enumerate(self._car.sensor_array.sensors) if s.detection]) - len(self._car.sensor_array.sensors) / 2

    def update(self, dt):
        error = self.get_line_position()

        if np.isnan(error):
            error = np.sign(self._last_error) * len(self._car.sensor_array.sensors) / 2
        self._last_error = error
        
        turn = self._pid.update(error, dt)

        left = right = 0.4
        left += turn
        right -= turn

        self._car.set_motors(left, right)
