"""
 构建优先级队列
"""
from common.data import JSONS
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # index保证同优先级元素的正确排序，否则优先级相同时会报TypeError
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop永远返回最小的元素
        return heapq.heappop(self._queue)[-1]


def run():
    queue = PriorityQueue()
    jsons = JSONS
    for json in jsons:
        queue.push(json, json['age'])
    print(queue.pop())
    print(queue.pop())


if __name__ == '__main__':
    run()