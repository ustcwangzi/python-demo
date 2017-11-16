"""
 按字段分组，要先排序再分组，因为groupby仅查找连续的相同元素
"""
from common.data import JSONS
from collections import defaultdict
import operator, itertools


def run():
    a = sorted(JSONS, key=operator.itemgetter('age'))
    print(a)
    for name, items in itertools.groupby(a):
        for item in items:
            print(item)
    # 如果仅是为了将数据分组到一起，可使用多值字典
    rows_by_date = defaultdict(list)
    for row in JSONS:
        rows_by_date[row['age']].append(row)
    print(rows_by_date)


if __name__ == '__main__':
    run()