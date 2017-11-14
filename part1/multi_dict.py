"""
 多值字典
"""
from collections import defaultdict


def run():
    dlist = defaultdict(list)
    dlist['a'].append(1)
    dlist['a'].append(1)
    dlist['a'].append(2)
    dlist['b'].append(4)
    for key in dlist:
        print(key, dlist[key])

    dset = defaultdict(set)
    dset['a'].add(1)
    dset['a'].add(1)
    dset['a'].add(2)
    dset['b'].add(3)
    for key in dset:
        print(key, dset[key])


if __name__ == '__main__':
    run()