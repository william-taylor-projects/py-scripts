
# OO in Python

class Point2:
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value    
   
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0},{1})".format(self.x, self.y)

    def __str__(self):
        return "Point({0},{1})".format(self.x, self.y)

class Point3(Point2):
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def __eq__(self, other):
        return self.z == other.z and super().__eq__(other)

    def __add__(self, other):
        raise NotImplementedError()

    def __repr__(self):
        return "Point({0},{1},{2})".format(self.x, self.y, self.z)

    def __str__(self):
        return "Point({0},{1},{2})".format(self.x, self.y, self.z)


a = Point2(10, 10)
b = Point2(10, 10)
c = Point3(10, 10, 10)

print(a == b)
print(str(a))
print(str(c))
#print(c + c)

c.x = 5
c.y = 10
c.z = 15
print(c.x, c.y, c.z)