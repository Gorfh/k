class Item:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

class Item2(Item):
    pass

item1 = Item(5)
item2 = Item(3)

print(item1 + item2)
print(item1 - item2)
print(item1 * item2)
print(item1 / item2)
item3 = Item2(2)
item4 = Item2(2)
print(item3 + item4)
print(item3 - item4)
print(item3 * item4)
print(item3 / item4)