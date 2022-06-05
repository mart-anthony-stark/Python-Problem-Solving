from cmath import sqrt
from unicodedata import name


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "-"

    def getDistance(self, other) -> float:
        difX = self.x - other.x
        difY = self.y - other.y
        x = pow(difX, 2)
        y = pow(difY, 2)
        return sqrt(x+y).real


class Inuman:
    def __init__(self, point: Point, number: int, name: str, price: float) -> None:
        self.x = point.x
        self.y = point.y
        self.number = number
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.number


class Person:
    def __init__(self, point: Point, name: str, money: str, inumanList: list) -> None:
        self.x = point.x
        self.y = point.y
        self.name = name
        self.money = money
        self.inumanList = inumanList

    def __str__(self) -> str:
        return self.name[0]


p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1)
print(p1.getDistance(p2))
