"""
 时间与字符串的转换
"""
from datetime import datetime


# strptime性能较差, 若已知时间格式为YYYY-MM_DD,可自定义解析
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


def run():
    text = '2017-10-10'
    print(datetime.strptime(text, '%Y-%m-%d'))

    d = datetime(2017, 10, 10)
    print(datetime.strftime(d, '%A %B %d, %Y'))

    # 自定义
    print(parse_ymd(text))


if __name__ == '__main__':
    run()
