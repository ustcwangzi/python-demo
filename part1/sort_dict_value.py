"""
 对字典的值进行排序／查找最大最小值等操作
 zip创建的是一个只能访问一次的迭代器，不可创建后，先max再min
"""
from common.data import PRICES


def run():
    prices = PRICES
    for k, v in prices.items():
        print(k, v)
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    sort_price = sorted(zip(prices.values(), prices.keys()))
    print("min_price", min_price)
    print("max_price", max_price)
    print("sort_price", sort_price)


if __name__ == '__main__':
    run()