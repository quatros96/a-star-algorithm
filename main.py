from copy import Error
import sys

from graph import Graph

# All assigment files are provided in graphs/ folder. Any custom file should be placed there to work.
# run: python main.py <file name>

fileName: str = ''
# check if user provided filename
try:
    fileName = sys.argv[1]
except IndexError:
    print('File was not specified!')

# run algorithm and output the result (format specified by assignment)
if len(fileName) > 0:
    graph: Graph = Graph(fileName)
    result = graph.aStar()
    if len(result) > 0:
        resultStringList = [str(x) for x in result]
        print(' '.join(resultStringList))
    else:
        print('Brak')
