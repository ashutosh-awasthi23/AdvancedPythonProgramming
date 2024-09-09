class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, name, r):
        self.r = r

    def area(self):
        return f"{3.14 * self.r**2}"


class Rectangle(Shape):
    def __init__(self, name, le, b):
        self.le = le
        self.b = b

    def area(self):
        return f"{self.le * self.b}"


def print_shape_area(shape):
    print(f"The area of shape is: {shape.area()}")


if __name__ == '__main__':
    circle = Circle("circle", 3)
    rect = Rectangle("rectangle", 3, 4)

    print_shape_area(circle)
    print_shape_area(rect)


