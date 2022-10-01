from pyfollow.world import WorldElement, Vector, Transform


class Board(WorldElement):
    def __init__(self, transform: Transform, parent: WorldElement):
        scale = 0.5
        polygon = [
            Vector(0, 0).mul(scale),
            Vector(0, 1).mul(scale),
            Vector(1, 1).mul(scale),
            Vector(1, 0.5).mul(scale),
            Vector(0.5, 0.5).mul(scale),
            Vector(0.5, 1.5).mul(scale),
            Vector(1.5, 1.5).mul(scale),
            Vector(1.5, 0).mul(scale),

        ]
        super().__init__(polygon, transform, parent)
