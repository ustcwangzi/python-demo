"""
 通过字符串调用方法
 使用functools.total_ordering只需定义一个__eq__
 外加一个其他方法(__lt__, __le__, __gt__, __ge__)中的一个即可
 装饰器会自动为你填充其他比较方法
"""
from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name):
        self.name = name
        self.rooms = list()

    def __str__(self):
        return '{}: {} square foot'.format(self.name,self.space)

    def add_room(self, room):
        self.rooms.append(room)

    @property
    def space(self):
        return sum(r.square_feet for r in self.rooms)

    def __eq__(self, other):
        return self.space == other.space

    def __lt__(self, other):
        return self.space < other.space


if __name__ == '__main__':
    h1 = House('h1')
    h1.add_room(Room('Tom', 14, 12))
    h1.add_room(Room('Tony', 11, 12))
    h2 = House('h2')
    h2.add_room(Room('Kit', 10, 28))
    houses = [h1, h2]
    print(h1 > h2)
    print(h1 < h2)
    print(h1 == h2)
    print(min(houses))

