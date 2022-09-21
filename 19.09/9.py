# -- coding: utf-8 --
def printIsChocolateBreakable(n, m, k):
  if (k % n == 0 or k % m == 0):
    print('Yes')
    return
  print('No')

printIsChocolateBreakable(3, 4, 8)
printIsChocolateBreakable(3, 4, 3)
printIsChocolateBreakable(3, 4, 4)
printIsChocolateBreakable(3, 4, 6)
printIsChocolateBreakable(3, 4, 9)
printIsChocolateBreakable(3, 4, 12)
printIsChocolateBreakable(3, 4, 2)
printIsChocolateBreakable(3, 4, 5)
printIsChocolateBreakable(3, 4, 1)
printIsChocolateBreakable(3, 4, 13)
