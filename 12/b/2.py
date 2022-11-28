# -*- coding: utf-8 -*-

def problem():
    n = int(input())

    if n == 0:
        return [float('-inf')]

    return sorted([n] + problem())


def main():
    print(problem()[-2])


if __name__ == '__main__':
    main()
