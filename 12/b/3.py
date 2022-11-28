# -*- coding: utf-8 -*-

def problem(counter = 0, nums = []):
    n = int(input())

    if n != 0:
        counter += 1
        if counter & 1:
            nums.append(n)

        problem(counter, nums)
    else:
        for num in nums:
            print(num)


def main():
    problem()


if __name__ == '__main__':
    main()
