# -*- coding: utf-8 -*-

def problem(n, divider = 2):
    if n <= 2 or divider ** 2 > n:
        return True

    if n % divider == 0:
        return False

    return problem(n, divider = divider + 1)


def problem_n(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    print('YES' if problem(int(input('N: '))) else 'NO')


if __name__ == '__main__':
    main()
