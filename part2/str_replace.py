"""
 字符串替换
"""
from common.data import LINES
import re


def change_data(val):
    return '999'


def run():
    # 适用于简单替换
    a = LINES.replace('a', 'z')
    print(a)

    # 适用于复杂替换，(匹配模式, 替换模式, str)
    b = re.sub(r'(\d+)', r'999', LINES)
    print(b)

    # 支持回调
    pattern = re.compile(r'(\d+)')
    c = pattern.sub(change_data, LINES)
    print(c)

    # 返回被替换的字符串个数
    d = re.subn(r'(\d+)', r'999', LINES)
    print(d)


if __name__ == '__main__':
    run()
