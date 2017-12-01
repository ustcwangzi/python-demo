"""
 排列组合
"""
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def run():
    items = ['a', 'b', 'c']
    # 全排列
    for item in permutations(items):
        print(item)

    # 指定长度
    for item in permutations(items, 2):
        print(item)

    # 组合，不重复，即(a,b)与(b,a)一样
    for item in combinations(items, 2):
        print(item)

    # 组合，重复选择，允许统一元素选择多次
    for item in combinations_with_replacement(items, 2):
        print(item)


if __name__ == '__main__':
    run()
