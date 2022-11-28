# -*- coding: utf-8 -*-

def problem(n, divider = 2):
    if n <= 2 or divider ** 2 > n:
        return True

    if n % divider == 0:
        return False

    return problem(n, divider = divider + 1)


def main():
    print(problem(int(input('N: '))))


if __name__ == '__main__':
    main()
