# -- coding: utf-8 --
def printIsLeapYear(year):
  if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('Yes')
    return
  print('No')

printIsLeapYear(2004)
printIsLeapYear(1999)
printIsLeapYear(2000)
printIsLeapYear(1900)
