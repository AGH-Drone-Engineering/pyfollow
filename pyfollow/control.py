import numpy as np
from pyfollow.pid import PID


class ControlSystem:
    def __init__(self, car):
        self._car = car
        self._pid = PID(0.1, 0.0)
        self._last_turn = 0

    def get_line_position(self):
        return np.mean([i for i, s in enumerate(self._car.sensor_array.sensors) if s.detection]) - len(self._car.sensor_array.sensors) / 2

    def update(self, dt):
        error = self.get_line_position()


        if np.isnan(error):
            turn = np.sign(self._last_turn) * 0.4
        else:
            turn = self._pid.update(error, dt)

        self._last_turn = turn

        left = right = 0.4
        left += turn
        right -= turn

        self._car.set_motors(left, right)
