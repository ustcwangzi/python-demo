"""
 跳过开始部分的迭代器
"""
from common.data import ITEMS
from itertools import dropwhile
from itertools import islice


def run():
    # dropwhile丢弃函数返回False之前的所有元素，之后的元素不再执行过滤（即使满足丢弃条件）
    with open('../common/test') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

    # 明确知道了要跳过的元素个数使用islice
    for x in islice(ITEMS, 3, None):
        print(x)


if __name__ == '__main__':
    run()
