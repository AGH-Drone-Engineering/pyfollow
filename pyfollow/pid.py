class PID:
    def __init__(self, p, d):
        self._p = p
        self._d = d
        self._last_error = 0

    def update(self, error, dt):
        p = self._p * error
        d = self._d * (error - self._last_error) / dt
        self._last_error = error
        return p + d
