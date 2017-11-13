"""
 获取最大／最小的N个元素
"""
from common.data import RECORDS
from common.data import JSONS
import heapq


def run():
    records = RECORDS
    # 内部使用heapify构造了一个大根／小根堆
    print("最小的两个:", heapq.nsmallest(2, records))
    print("最大的两个:", heapq.nlargest(2, records))
    jsons = JSONS
    print("最小的两个:", heapq.nsmallest(2, jsons, key=lambda p: p['age']))
    print("最大的两个:", heapq.nlargest(2, jsons, key=lambda p: p['age']))


if __name__ == '__main__':
    run()