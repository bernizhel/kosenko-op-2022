# -*- coding: utf-8 -*-

def problem(a, b, init = True, step = 1):
    if init:
        step = -step if a > b else step
        init = False

    if a != b + step:
        print(a)
        problem(a + step, b, init = init, step = step)


def main():
    problem(int(input('A: ')), int(input('B: ')))


if __name__ == '__main__':
    main()
