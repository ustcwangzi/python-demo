"""
 使用类方法实现多个构造函数
"""
import time


class DateUtil:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


def run():
    a = DateUtil(2018, 1, 20)
    print(a.year, a.month, a.day)

    b = DateUtil.today()
    print(b.year, b.month, b.day)


if __name__ == '__main__':
    run()
