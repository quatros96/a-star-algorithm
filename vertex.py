import typing as type

# simple Vertex class to easy


class Vertex:
    name: int
    position: type.Tuple[int, int]

    # constructor
    def __init__(self, name: int, position: type.Tuple[int, int]) -> None:
        self.name = name
        self.position = position

    # equality function - for comparing instances of this class
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Vertex):
            return NotImplemented

        return self.name == o.name

    # string representation of the instance
    def __repr__(self) -> str:
        return 'Vertex(%s, x: %s, y: %s)' % (self.name, self.position[0], self.position[1])
