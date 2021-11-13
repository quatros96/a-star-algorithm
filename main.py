from copy import Error
import sys

from graph import Graph

fileName: str = ''
try:
    fileName = sys.argv[1]
except IndexError:
    print('File was not specified!')

if len(fileName) > 0:
    graph: Graph = Graph(fileName)
    result = graph.aStar()
    if len(result) > 0:
        resultStringList = [str(x) for x in result]
        print(' '.join(resultStringList))
    else:
        print('Brak')
