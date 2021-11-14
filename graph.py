import math
import typing as type
from math import dist

from fileReader import FileReader
from vertex import Vertex

# class for graph that can run a* algorithm on itself


class Graph:
    _vertexesList: type.List[type.Tuple[int, int]]
    _vertexes: type.List[Vertex] = []
    _start: Vertex
    _end: Vertex
    _adjacencyMatrix: type.List[type.List[float]]
    _fileReader: FileReader

    # constructor
    def __init__(self, fileName: str) -> None:
        self._fileReader = FileReader(fileName)
        startName: int
        endName: int
        self._vertexesList, startName, endName, self._adjacencyMatrix = self._fileReader.readSelectedFile()
        self._start = Vertex(startName, self._vertexesList[startName - 1])
        self._end = Vertex(endName, self._vertexesList[endName - 1])
        self._prepareVertexes()

    # generate list of Vertex instances
    def _prepareVertexes(self) -> None:
        for count, vertex in enumerate(self._vertexesList):
            self._vertexes.append(Vertex(count + 1, vertex))

    # generate dict with every vertex name as key and value as infinity
    def _generateVertexNameToValueDict(self) -> type.Dict[int, float]:
        result: type.Dict[int, float] = {}
        for vertex in self._vertexes:
            result[vertex.name] = float('inf')
        return result

    # finding neighbours of specified Vertex based on adjacency matrix
    def _findNeighboursOf(self, vertex: Vertex) -> type.List[Vertex]:
        result: type.List[Vertex] = []
        for count, value in enumerate(self._adjacencyMatrix[vertex.name - 1]):
            if value != 0:
                match = [x for x in self._vertexes if x.name == count + 1]
                result.append(match[0])
        return result

    # Heuristic function - eucliedian distance for this project
    def _h(self, vertex: Vertex) -> float:
        return dist(vertex.position, self._end.position)

    # find Vertex with smallest value of f(vertex) function. f(vertex) = h(vertex) + g(vertex)
    def _findVertexWithSmallestFFrom(self, vertexes: type.List[Vertex], g: type.Dict[int, float]) -> Vertex:
        vertexWithSmallestF: Vertex = vertexes[0]
        for vertex in vertexes:
            if self._h(vertex) + g[vertex.name] < self._h(vertexWithSmallestF) + g[vertexWithSmallestF.name]:
                vertexWithSmallestF = vertex
        return vertexWithSmallestF

    # finding edge weight between two vertexes
    def _getEdgeWeight(self, vertex1name: int, vertex2name: int) -> float:
        return self._adjacencyMatrix[vertex1name - 1][vertex2name - 1]

    # path reconstruction based on cameFrom dictionary. Key is vertex we are in and value is vertex we came from.
    def _pathReconstruction(self, cameFrom: type.Dict[int, int]) -> type.List[int]:
        endName: int = self._end.name
        currentName = endName
        result: type.List[int] = [endName]
        while currentName != self._start.name:
            result.append(cameFrom[currentName])
            currentName = cameFrom[currentName]
        result.reverse()
        return result

    # implementation of full A* algorithm
    def aStar(self) -> type.List[int]:
        workingPoints: type.List[Vertex] = [self._start]
        cameFrom: type.Dict[int, int] = {}
        g: type.Dict[int, float] = self._generateVertexNameToValueDict()
        g[self._start.name] = 0
        f: type.Dict[int, float] = self._generateVertexNameToValueDict()
        f[self._start.name] = self._h(self._start)

        while len(workingPoints) > 0:
            x: Vertex = self._findVertexWithSmallestFFrom(workingPoints, g)
            if x == self._end:
                return self._pathReconstruction(cameFrom)
            workingPoints.remove(x)
            for neighbour in self._findNeighboursOf(x):
                temp_g = g[x.name] + \
                    self._getEdgeWeight(x.name, neighbour.name)
                if temp_g < g[neighbour.name]:
                    cameFrom[neighbour.name] = x.name
                    g[neighbour.name] = temp_g
                    f[neighbour.name] = g[neighbour.name] + self._h(neighbour)
                    if neighbour not in workingPoints:
                        workingPoints.append(neighbour)
        return []
