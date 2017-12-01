"""
 同时迭代多个序列
"""
from itertools import zip_longest
from itertools import chain


def run():
    # 交替迭代
    a = [1, 5, 4, 2, 10, 7]
    b = [101, 78, 37, 15, 62, 99]
    for x, y in zip(a, b):
        print(x, y)

    # 默认是按最短长度
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a, b):
        print(i)

    # 按最长长度进行迭代，填充None
    for i in zip_longest(a, b):
        print(i)
    # 按最长长度进行迭代，填充0
    for i in zip_longest(a, b, fillvalue=0):
        print(i)

    # 依次迭代
    for i in chain(a, b):
        print(i)


if __name__ == '__main__':
    run()
