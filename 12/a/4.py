# -*- coding: utf-8 -*-

def problem(n):
    if n <= 0:
        return n

    return n % 10 + problem(n // 10)


def main():
    n = int(input('N: '))

    print(problem(n))


if __name__ == '__main__':
    main()
