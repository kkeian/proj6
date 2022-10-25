# /**
# *File Name: proj_6_lib.py
# *Academic Integrity Statement: I certify that, while others may have assisted me in brain storming, debugging and validating this program, the program itself is my own work. I understand that submitting code which is the work of other individuals is a violation of the course Academic Integrity Policy and may result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. I also understand that if I knowingly give my original work to another individual that it could also result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. See Academic Integrity Procedural GuidelinesLinks to an external site. at:  https://psbehrend.psu.edu/intranet/faculty-resources/academic-integrity/academic-integrity-procedural-guidelinesLinks to an external site.
# *Assisted by and Assisted line numbers:
# *Your Name: Keian Kaserman
# *Your PSU user ID:  knk5281
# *Course title CMPSC 465
# *Due Time: 11:59PM, Sunday, October 30, 2022
# *Time of Last Modification: 7:27AM, Tuesday, October 25, 2022
# *Description: Utility functions for finding the largest square of all 1's in a given input matrix.
# */
def getLines(file):
  with open(file) as f:
    lines = f.readlines()
  return lines


def trimLines(lines):
  for i in range(len(lines)):
    lines[i] = lines[i].strip().split(' ')


def getMatrixSize(input):
  for line in input:
    if len(line) == 2:
      return int(line[0]), int(line[1])


def getMatrix(input):
  if input[0][0] == '':
    input.pop(0)
    if input[0][0] == '0':
      input.pop(0)
      return None

  height, width = getMatrixSize(input)
  input.pop(0)
  matrix = []
  for h in range(height):
    row = input.pop(0)
    matrix.append(row)

  return matrix


def getAdjacentSquares(index, matrixSize):
  column, row = index
  columnSize, rowSize = matrixSize

  top, bot = (column-1, row), (column+1, row)
  left, right = (column, row-1), (column, row+1)

  # Check if computed adjacent squares
  # are in valid ranges
  if row == 0:
    top = None
  elif row == columnSize -1:
    bot = None

  if left[1] < 0:
    left = None
  elif right[1] == rowSize:
    right = None

  return top, bot, left, right


def getLargestSquare(matrix):
  matrixSize = (len(matrix)-1, len(matrix[0]-1))
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == '1':
        index = j, i
        top, bot, left, right = getAdjacentSquares(index, matrixSize)

  # Objective function

  # Recursive case
  pass


def printOutput(out):
  for o in out:
    print(0)