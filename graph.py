import typing as type
from fileReader import FileReader
from copy import deepcopy


class Graph:
    _vertexes: type.List[type.Tuple[int, int]]
    _start: type.Tuple[int, int]
    _end: type.Tuple[int, int]
    _adjacencyMatrix: type.List[type.List[float]]
    _fileReader: FileReader

    currentVertex: type.Tuple[int, int]

    def __init__(self, fileName: str) -> None:
        self._fileReader = FileReader(fileName)
        self._vertexes, self._start, self._end, self._adjacencyMatrix = self._fileReader.readSelectedFile()
        self.currentVertex = deepcopy(self._start)

    def findNeighboursOf(self, vertex: type.Tuple[int, int]) -> type.List[type.Tuple[int, int]]:
        pass
