class ImmutablePoint:
    __slots__ = ('_x', '_y')  # Prevent creating new attributes

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
