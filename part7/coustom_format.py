"""
 对象自定义格式化
"""


_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


def run():
    d = Date(2017, 12, 12)
    print(d)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))


if __name__ == '__main__':
    run()
