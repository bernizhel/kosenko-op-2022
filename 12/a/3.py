# -*- coding: utf-8 -*-

def problem(a):
    a = str(a)
    if len(a) <= 1:
        return a

    return a[-1] + problem(a[:-1])


def main():
    a = int(input('A: '))

    print(problem(a))


if __name__ == '__main__':
    main()
