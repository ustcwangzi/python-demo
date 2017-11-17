"""
 元素过滤，过滤列表或字典
"""
from common.data import NUMBERS, WORDS, COUNTS
from itertools import compress


def filterNubmer(val):
    if val > 5:
        return True
    else:
        return False


def run():
    # 方法简单，但当列表较大时会产生一个很大的结果集，占用大量内存
    a = [n for n in NUMBERS if n > 5]
    print(a)
    b = [n if n > 5 else 0 for n in NUMBERS]
    print(b)

    # filter可解决上述缺点
    c = list(filter(filterNubmer, NUMBERS))
    print(c)

    # 也可使用compress过滤，需要接收一个Boolean序列来判断哪些元素符合
    selector = [n > 5 for n in NUMBERS]
    d = list(compress(WORDS, selector))
    print(d)

    # 过滤字典
    e = {key: value for key, value in COUNTS.items() if value > 5}
    print(e)


if __name__ == '__main__':
    run()