from cmath import sqrt


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
    def __init__(self, point, number, name, price) -> None:
        self.x = point.x
        self.y = point.y
        self.number = number
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return self.number


p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1)
print(p1.getDistance(p2))
