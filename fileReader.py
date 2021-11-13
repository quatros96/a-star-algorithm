import typing as type
import fnmatch
from os import listdir
from os.path import isfile, join


class FileReader:
    _graphsDir: str = './graphs'
    _selectedFile: str = ''

    def __init__(self, fileName: str) -> None:
        self._selectedFile = fileName

    def getDirectoryGraphFiles(self) -> type.List[str]:
        foundGraphFiles = [file for file in listdir(self._graphsDir) if (
            isfile(join(self._graphsDir, file)) and fnmatch.fnmatch(file, '*.txt'))]
        return foundGraphFiles

    def selectFile(self) -> None:
        success: bool = False
        avaliableFiles: type.List[str] = self.getDirectoryGraphFiles()
        print('Avaliable files: ', avaliableFiles)
        while not success:
            self._selectedFile: str = input('Type in file name: ')
            if self._selectedFile in avaliableFiles:
                success = True
            else:
                print('This file does not exist! Try again...')

    def readSelectedFile(self) -> type.Tuple[type.List[type.Tuple[int, int]
                                                       ], int, int, type.List[type.List[float]]]:
        try:
            if self._selectedFile == '' or self._selectedFile not in self.getDirectoryGraphFiles():
                raise Exception('Invalid file or file is not provided!')
            with open(self._graphsDir + '/' + self._selectedFile) as file:
                try:
                    vertexes: type.List[type.Tuple[int, int]
                                        ] = self.readVertexesFromFile(file)
                    startEnd: type.Tuple[int,
                                         int] = self.readStartEndFromFile(file)
                    start: int = startEnd[0]
                    end: int = startEnd[1]
                    adjacencyMatrix: type.List[type.List[float]
                                               ] = self.readAdjacencyMatrixFromFile(file)
                    return vertexes, start, end, adjacencyMatrix
                except Exception as e:
                    print(e)
        except EnvironmentError as filErr:
            print('File error!: ', filErr)
        return vertexes, start, end, adjacencyMatrix

    def readVertexesFromFile(self, file: type.TextIO) -> type.List[type.Tuple[int, int]]:
        line: str = file.readline()
        vertexesStringList: type.List[str] = line.replace(', ', ',').split(' ')
        if len(vertexesStringList) < 2:
            raise Exception('Not enough vertexes!')
        result: type.List[type.Tuple[int, int]] = []
        for vertexString in vertexesStringList:
            vertexValues: type.List[str] = vertexString.strip().replace(
                ' ', '').replace('(', '').replace(')', '').split(',')
            vertexTuple: type.Tuple[int, int] = (
                int(vertexValues[0]), int(vertexValues[1]))
            result.append(vertexTuple)
        return result

    def readStartEndFromFile(self, file: type.TextIO) -> type.Tuple[int, int]:
        line: str = file.readline().strip()
        values: type.List[str] = line.split(' ')
        if len(values) < 2:
            raise Exception('Start or end point not specified!')
        valuesTuple: type.Tuple[int, int] = (int(values[0]), int(values[1]))
        return valuesTuple

    def readAdjacencyMatrixFromFile(self, file: type.TextIO) -> type.List[type.List[float]]:
        lines: type.List[str] = file.readlines()
        result: type.List[type.List[float]] = []
        for line in lines:
            stringValues: type.List[str] = line.strip().split(' ')
            values: type.List[float] = [float(value) for value in stringValues]
            result.append(values)
        for values in result:
            if len(values) != len(result):
                raise Exception('Matrix is not square!')
        return result
