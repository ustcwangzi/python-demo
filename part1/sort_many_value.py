"""
 多字段排序
"""
from common.data import JSONS
import operator


def run():
    # 这种方式相对速度快，也适用于min／max等
    a = sorted(JSONS, key=operator.itemgetter('name', 'age'))
    print(a)
    b = sorted(JSONS, key=lambda r: (r['name'], r['age']))
    print(b)


if __name__ == '__main__':
    run()