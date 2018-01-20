"""
 绕过init创建实例／对象
"""
import time


class DateUtil:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


def run():
    # 绕过init创建实例
    a = {'year': 2018, 'month': 1, 'day': 20}
    d = DateUtil.__new__(DateUtil)
    for k, v in a.items():
        setattr(d, k, v)
    print(d.year, d.month, d.day)

    # 绕过init创建对象
    b = DateUtil.today()
    print(b.year, b.month, b.day)


if __name__ == '__main__':
    run()
