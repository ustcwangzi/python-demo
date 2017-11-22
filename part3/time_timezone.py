"""
 时区
"""
from datetime import datetime, timedelta
from pytz import timezone
import pytz


def run():
    d = datetime(2017, 10, 10, 9, 30, 0)
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # 对时区时间操作，一个普遍策略是先转换为UTC时间，使用UTC时间来进行计算
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)

    later_utc = utc_d + timedelta(minutes=30)
    # 转回到本地时间
    print(later_utc.astimezone(central))


if __name__ == '__main__':
    run()
