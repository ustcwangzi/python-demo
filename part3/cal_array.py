"""
 利用numpy执行数组运算
"""
import numpy as np


def f(x):
    return 3 * x ** 2 - 2 * x + 7


def run():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    # Numpy arrays
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + ay)
    print(ax * ay)

    print(f(ax))
    print(np.cos(ax))


if __name__ == '__main__':
    run()
