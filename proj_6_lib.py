# /**
# *File Name: proj_6_lib.py
# *Academic Integrity Statement: I certify that, while others may have assisted me in brain storming, debugging and validating this program, the program itself is my own work. I understand that submitting code which is the work of other individuals is a violation of the course Academic Integrity Policy and may result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. I also understand that if I knowingly give my original work to another individual that it could also result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. See Academic Integrity Procedural GuidelinesLinks to an external site. at:  https://psbehrend.psu.edu/intranet/faculty-resources/academic-integrity/academic-integrity-procedural-guidelinesLinks to an external site.
# *Assisted by and Assisted line numbers:
# *Your Name: Keian Kaserman
# *Your PSU user ID:  knk5281
# *Course title CMPSC 465
# *Due Time: 11:59PM, Sunday, October 30, 2022
# *Time of Last Modification: 16:48AM, Sunday, October 30, 2022
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


def printOutput(out):
  for o in out:
    print(o)

