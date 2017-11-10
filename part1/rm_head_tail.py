"""
 去除最大和最小的元素
"""
from common.data import RECORDS


def run():
    records = sorted(RECORDS)
    head, *middle, tail = records
    print('records: ', records)
    print('head: ', head)
    print('middle: ', middle)
    print('tail: ', tail)


if __name__ == '__main__':
    run()