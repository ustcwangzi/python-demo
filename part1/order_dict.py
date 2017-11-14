"""
 排序字典
 OrderedDict保持key的插入顺序，但大小是普通dict的两倍
"""
from collections import OrderedDict


def run():
    d = OrderedDict()
    d['b'] = 4
    d['a'] = 1
    d['c'] = 3
    for key in d:
        print(key, d[key])


if __name__ == '__main__':
    run()