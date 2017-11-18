"""
 删除指定字符
"""
from common.data import TEXTS
import re


def run():
    # 删除开始和结尾的空字符
    print(TEXTS.strip())
    # 删除开始的空字符
    print(TEXTS.lstrip())
    # 删除结尾的空字符
    print(TEXTS.rstrip())

    # 处理中间字符
    print(TEXTS.replace(' ', ''))
    print(re.sub('\s+', '', TEXTS))


if __name__ == '__main__':
    run()
