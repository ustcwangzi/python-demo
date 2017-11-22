"""
 时间／时间段的加减
"""
from datetime import datetime, timedelta


def run():
    # 时间段
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # 时间
    a = datetime(2017, 10, 10)
    b = datetime(2017, 12, 21)
    print(a + timedelta(days=22))
    print(b - a)

    # 当前时间
    print(datetime.today())


if __name__ == '__main__':
    run()
