import typing as type


class Vertex:
    name: int
    position: type.Tuple[int, int]

    def __init__(self, name: int, position: type.Tuple[int, int]) -> None:
        self.name = name
        self.position = position

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Vertex):
            return NotImplemented

        return self.name == o.name

    def __repr__(self) -> str:
        return 'Vertex(%s, x: %s, y: %s)' % (self.name, self.position[0], self.position[1])
