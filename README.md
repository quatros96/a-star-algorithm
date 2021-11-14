# A\* algorithm!

Hi! This project features A\* path finding algorithm. It works on directed and undirected graphs.
Sample files are provided in graphs/ catalog.

# Input

Files must be .txt in format specified below.

## Vertexes

First line features vertexes that graph is made of.

    (0, 0) (0, 1) (1, 0) (1, 1)

Later in algorithm (0, 0) vertex is recognized as number 1. (1, 1) is 4.

## Start & End Vertex

These points are specified by they given number.

    1 4

That means starting vertex is (0, 0) and end vertex is (1, 1).

## Graph representation

Graph is represented as adjacency matrix.

    0.000 1.000 0.000 1.414
    1.000 0.000 1.414 0.000
    0.000 1.414 0.000 1.000
    1.414 0.000 1.000 0.000

## Sample file

    (0, 0) (0, 1) (1, 0) (1, 1)
    1 4
    0.000 1.000 0.000 1.414
    1.000 0.000 1.414 0.000
    0.000 1.414 0.000 1.000
    1.414 0.000 1.000 0.000

# Output

Sample output

    1 10 5 8 11 19

These are vertex numbers as path that was designated by the algorithm.

# Run

Make sure you are in a project root directory.

    python main.py yourfilename.txt
