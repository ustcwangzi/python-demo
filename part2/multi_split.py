"""
 多分隔符分割字符串
"""
from common.data import LINES
import re


def run():
    # str.split只适用于单分隔符
    a = LINES.split(';')
    print(a)
    b = re.split(r'[,;\s]\s*', LINES)
    print(b)

    # 使用捕获分组时，分隔符也会输出
    c = re.split(r'(,|;|\s)\s*', LINES)
    print(c)


if __name__ == '__main__':
    run()
