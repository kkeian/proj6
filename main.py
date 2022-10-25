from proj_6_lib import getLines, trimLines, getMatrix, getLargestSquare
from proj_6_lib import printOutput
from copy import deepcopy

lines = getLines('input.txt')
trimLines(lines)
originalInput = deepcopy(lines)

largestSquares = []
matrix = getMatrix(lines)
while matrix is not None:
  # Computations
  largestSquares.append(getLargestSquare(matrix))

  matrix = getMatrix(lines)

printOutput(largestSquares)