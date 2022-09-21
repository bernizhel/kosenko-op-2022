# -- coding: utf-8 --
def getColorNumber(column, row):
  if (column % 2 and row % 2):
    return 1
  elif (not (column % 2) and not (row % 2)):
    return 1
  return 0

def printIsColorTheSame(firstColumn, firstRow, secondColumn, secondRow):
  if (getColorNumber(firstColumn, firstRow) == getColorNumber(secondColumn, secondRow)):
    print('Yes')
    return
  print('No')

printIsColorTheSame(1, 1, 1, 2)
printIsColorTheSame(1, 2, 1, 2)
printIsColorTheSame(2, 1, 1, 2)
printIsColorTheSame(2, 2, 1, 1)
