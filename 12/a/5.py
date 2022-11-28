# -*- coding: utf-8 -*-

def problem(a):
    print(a % 10, end = ' ')

    if a // 10 != 0:
        problem(a // 10)
    else:
        print()


def main():
    problem(int(input('N: ')))


if __name__ == '__main__':
    main()
