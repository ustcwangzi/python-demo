"""
 多序列排序
"""
from heapq import merge


def run():
    # 输入序列必须有序，merge不对序列进行排序，只检查所有序列的开始部分，并返回最小的那个元素
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in merge(a, b):
        print(c)


if __name__ == '__main__':
    run()
