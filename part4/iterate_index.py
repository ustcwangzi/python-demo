"""
 获得元素索引
"""
from common.data import ITEMS


def run():
    # 从0开始
    for idx, val in enumerate(ITEMS):
        print(idx, val)

    # 从指定索引开始
    for idx, val in enumerate(ITEMS, 1):
        print(idx, val)

    # 序列中含有元组的解压
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for n, (x, y) in enumerate(data):
        print(n)
        print(x, y)


if __name__ == '__main__':
    run()
