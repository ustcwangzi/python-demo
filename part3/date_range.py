"""
 时间范围生成器
"""
from datetime import datetime, timedelta


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def run():
    for d in date_range(datetime(2017, 10, 1), datetime(2017, 10, 10), timedelta(hours=6)):
        print(d)


if __name__ == '__main__':
    run()
