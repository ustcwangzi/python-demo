"""
 对自定义的类进行排序
"""
import operator


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return 'User({},{})'.format(self.name, self.id)


def run():
    users = [User('wang', 1), User('zhao', 4), User('chen', 3), User('wang', 2)]
    # 这种方式相对速度快，也适用于min／max等
    a = sorted(users, key=operator.attrgetter('id', 'name'))
    print(a)
    b = sorted(users, key=lambda r: (r.id, r.name))
    print(b)


if __name__ == '__main__':
    run()