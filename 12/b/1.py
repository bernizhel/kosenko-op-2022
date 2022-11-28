# -*- coding: utf-8 -*-

def problem():
    n = int(input())

    if n == 0:
        return float('-inf')

    return max([n, problem()])


def main():
    print(problem())


if __name__ == '__main__':
    main()
