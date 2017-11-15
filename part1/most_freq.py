"""
 计算出现频率最高的单词
"""
from common.data import WORDS
import collections


def run():
    word_count = collections.Counter(WORDS)
    print(word_count)
    top_two = word_count.most_common(2)
    print(top_two)


if __name__ == '__main__':
    run()