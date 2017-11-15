"""
 切片命名
"""
from common.data import LINES


def run():
    print(LINES[2:6])
    a = slice(2, 6)
    print(LINES[a])
    b = slice(2, 10, 2)
    print(LINES[b])
    print("start:", b.start, ",stop:", b.stop, ",step:", b.step)
    # indices将切片映射到确定大小的序列上，避免出现IndexError
    c = slice(2, 100, 3)
    print(c.indices(len(LINES)))


if __name__ == '__main__':
    run()