from pyfollow.world import Polygon, WorldElement, Vector, Transform


class Board(WorldElement):
    def __init__(self, transform: Transform, parent: WorldElement):
        scale = 0.5
        polygon = Polygon(
            points = [
                Vector(0, 0).mul(scale),
                Vector(0, 1).mul(scale),
                Vector(1, 1).mul(scale),
                Vector(1, 0.5).mul(scale),
                Vector(0.5, 0.5).mul(scale),
                Vector(0.5, 1.5).mul(scale),
                Vector(1.5, 1.5).mul(scale),
                Vector(1.5, 0).mul(scale),

            ],
            thickness = 0.019,
            color = (50, 50, 50),
        )
        super().__init__(polygon, transform, parent)
