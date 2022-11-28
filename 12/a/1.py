# -*- coding: utf-8 -*-

def problem(x, n, initial_x = 0):
    if initial_x == 0:
        initial_x = x

    if n <= 1:
        return x

    return problem(x * initial_x / n, n - 1, initial_x = x)


def main():
    x = int(input('X: '))
    n = int(input('N: '))

    print(problem(x, n))


if __name__ == '__main__':
    main()
