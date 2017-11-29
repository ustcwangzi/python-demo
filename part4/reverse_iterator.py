"""
 反向迭代
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    # 正向迭代
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def run():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    for rr in reversed(Countdown(5)):
        print(rr)

    for rr in Countdown(3):
        print(rr)


if __name__ == '__main__':
    run()
