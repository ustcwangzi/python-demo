"""
 计算当前月份时间范围
"""
from datetime import date, timedelta
from calendar import monthrange


def get_month_range(start_date=None):
    if start_date is None:
        # 对应月份的第一天
        start_date = date.today().replace(day=1)
    week, days_in_month = monthrange(start_date.year, start_date.month)
    print("本月共 %s 天, 第一天是周 %s" % (days_in_month, week + 1))
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


def run():
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day


if __name__ == '__main__':
    run()
