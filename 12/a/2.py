# -*- coding: utf-8 -*-

def problem(a, b):
    if a < b:
        return a

    return problem(a - b, b)


def main():
    a = int(input('A: '))
    b = int(input('B: '))

    print(problem(a, b))


if __name__ == '__main__':
    main()
