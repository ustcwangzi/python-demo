"""
 去除重复元素，保持原顺序
"""
from common.data import WORDS
from common.data import JSONS


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def run():
    result = dedupe(WORDS)
    print(list(result))
    result = dedupe(JSONS, key=lambda a: (a['name'], a['age']))
    print(list(result))


if __name__ == '__main__':
    run()