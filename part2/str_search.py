"""
 字符串查找
"""
from common.data import LINES, DATES, TEXTS
import re


def run():
    print(LINES.startswith('a'))
    print(LINES.endswith('b'))

    # 数字匹配
    if re.match(r'\d+/\d+/\d+', DATES):
        print('yes')
    else:
        print('no')

    # 编译模式
    pattern = re.compile(r'\d+/\d+/\d+')
    if pattern.match(DATES):
        print('yes')
    else:
        print('no')

    print(pattern.findall(TEXTS))

    # 使用捕获分组
    pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = pattern.match(DATES)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
    month, day, year = m.groups()
    print(month, day, year)
    print(pattern.findall(TEXTS))
    for month, day, year in pattern.findall(TEXTS):
        print('{}-{}-{}'.format(year, month, day))

    # 迭代方式返回匹配
    for m in pattern.finditer(TEXTS):
        print(m.groups())

    # 直接使用re模块函数
    a = re.findall(r'(\d+)/(\d+)/(\d+)', TEXTS)
    print(a)
    b = re.findall(r'python', LINES, flags=re.IGNORECASE)
    print(b)


if __name__ == '__main__':
    run()
