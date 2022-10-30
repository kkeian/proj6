from proj_6_lib import getLines, trimLines, getMatrix
from proj_6_lib import printOutput
from copy import deepcopy
# 
# File Name: main.py
# Academic Integrity Statement: I certify that, while others may have assisted me in brain storming, debugging and validating this program, the program itself is my own work. I understand that submitting code which is the work of other individuals is a violation of the course Academic Integrity Policy and may result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. I also understand that if I knowingly give my original work to another individual that it could also result in a zero credit for the assignment, or course failure and a report to the Academic Dishonesty Board. See Academic Integrity Procedural GuidelinesLinks to an external site. at:  https://psbehrend.psu.edu/intranet/faculty-resources/academic-integrity/academic-integrity-procedural-guidelinesLinks to an external site.
# Assisted by and Assisted line numbers:
# Your Name: Keian Kaserman
# Your PSU user ID:  knk5281
# Course title CMPSC 465
# Due Time: 11:59PM, Sunday, October 30, 2022
# Time of Last Modification: 16:49AM, Sunday, October 30, 2022
# Description: Main function for finding the largest square of all 1's in a given input matrix.
# 


lines = getLines('input.txt')
trimLines(lines)
originalInput = deepcopy(lines)

largestSquares = []

# Find largest square for each input matrix
matrix = getMatrix(lines)
while matrix is not None: # More matrices to process
  # Data Structures to hold largest sides
  # Will compute largest squares based off results here
  largestIndex = 0
  largestSquareSides = [largestIndex] # largest square is size 0 initially
  # We want the largest possible square size.
  # -----
  # If we haven't found any squares,
  # the largest possible square side
  # to find is 2 units in length.
  # Otherwise, it is 1 more than the largest square side found
  smallestSquareSide = 2
  largestSide = smallestSquareSide
  
  # For this matrix, we want to know how
  # many parts to process.
  rows = len(matrix)
  columns = len(matrix[0])
  # Process all elements (columns)
  # in a row before moving onto next row.
  for i in range(rows):
    for j in range(columns-1): # Don't do a check of last column
      if matrix[i][j] == '1': # Current element is marked
        possibleSquare = True
        # Now we need to check for presence of a larger square
        # than the largest one we've found so far.
        # This == side length 2 if none found, or
        # largest+1 if we've found a square.
        elemsToCheck = largestSide
        # Check down the column to the right of current elem
        # first
        nextColumn = j + 1
        # This will increment to move down
        # the column in checks
        currRow = i
        # To keep track of how many checks we've made
        # down column elements
        n = 0
        while n < elemsToCheck:
          # we don't want to try to check a row or column
          # beyond the bounds of matrix
          if currRow == rows:
            # No square possible if more checks to do
            # but we've reached the end of the matrix
            possibleSquare = False
            break

          elif matrix[currRow][nextColumn] == '1':
            # Move check to next element down in the
            # column.
            currRow += 1
            # Make sure to only do as many checks as needed.
            n += 1
          else:
            # Can't be a square because last element
            # checked was not filled.
            possibleSquare = False
            # Stop checking for square
            break

        if possibleSquare:
          # All elements in next column were filled out.
          # ---
          # Check elements in row below the element found
          currColumn = j # this will increment to check
          # all elements in row below found element but in reverse
          nextRow = i+1 if elemsToCheck == 2 else elemsToCheck -1 # skips already checked rows
          elemsToCheck -= 1 # accounts for bottom right square element checked
          # above in column checking loop
          n = 0
          while n < elemsToCheck and nextRow < rows:
            # We already checked the bottom right corner
            # of square and it passed if we're here. So
            # we don't re-check it, hence "elemsToCheck-1"
            # --
            # since we check in reverse, we can't exceed
            # bounds of columns.
            # But we make sure we can't exceed bounds of rows.
            if matrix[nextRow][currColumn] == '1':
              # Make next check be of the element to the
              # left of current check.
              currColumn -= 1
              # Keep track of checks performed
              n += 1
            else:
              # Can't be a square because last element we
              # checked was not filled.
              possibleSquare = False
              break

          if n == elemsToCheck and possibleSquare:
            # We searched all elements and
            # still possible square exists.
            # == Found square 
            largestSide = elemsToCheck+1
            # Store largest square side which has
            # to be equal to the number or elements
            # we checked in each column and row above
            largestSquareSides.append(largestSide)
            # Note the next largest possible square
            largestSide += 1
            # Track index of this largest square side found
            largestIndex += 1

  # Compute the largest found square and store it
  largestSide = largestSquareSides[largestIndex]
  largestSquares.append(largestSide*largestSide)

  # Get next matrix
  matrix = getMatrix(lines)

# Print, in order, the largest found squares for
# input matrices
printOutput(largestSquares)

# Sample Output:
# 4
# 9