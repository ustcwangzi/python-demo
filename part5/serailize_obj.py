"""
 对象序列化／反序列化
"""
import pickle
from common.data import ITEMS


def run():
    # 对象保存到文件
    f = open('/Users/wangzi/Downloads/temp', 'wb')
    pickle.dump(ITEMS, f)

    # 对象转存为字符串
    str = pickle.dumps(ITEMS)

    # 从文件中恢复对象
    f = open('/Users/wangzi/Downloads/temp', 'rb')
    print(pickle.load(f))

    # 从字符串恢复对象
    print(pickle.loads(str))


if __name__ == '__main__':
    run()
