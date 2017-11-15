"""
 获取dict中相同／不同的key／item
 value不支持这些操作
"""
from common.data import PRICES
from common.data import COUNTS


def run():
    same_key = PRICES.keys() & COUNTS.keys()
    print("same key: ", same_key)
    same_item = PRICES.items() & COUNTS.items()
    print("same item: ", same_item)
    diff_key = PRICES.keys() - COUNTS.keys()
    print("different key: ", diff_key)


if __name__ == '__main__':
    run()