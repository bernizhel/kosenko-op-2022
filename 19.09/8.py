# -- coding: utf-8 --
def findTheSame(a, b, c):
    differentNumbersAmount = len({a, b, c})
    if (differentNumbersAmount == 3):
        print(0)
    elif (differentNumbersAmount == 2):
        print(2)
    else:
        print(3)


findTheSame(1, 2, 3)
findTheSame(2, 2, 3)
findTheSame(1, 2, 1)
findTheSame(2, 3, 2)
findTheSame(1, 1, 1)
