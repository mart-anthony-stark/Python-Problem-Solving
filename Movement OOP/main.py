from cmath import sqrt


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        print("-")

    def getDistance(self, other) -> float:
        x = pow(2, self.x - other.x)
        y = pow(2, self.y - other.y)
        print(x)
        print(y)
        return sqrt(x+y)


p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.getDistance(p2))
