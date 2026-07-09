# Task 5: Extending a Class
import math

class Point:
    # init method / instances of class, attributes 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # equality, string representation, and Euclidian distance to another point.
    def __eq__(self, other):
            equal_x = self.x == other.x
            equal_y = self.y == other.y
            result = equal_x and equal_y
            return result

    def __str__(self):
            string_representation =  f"point({self.x}, {self.y})"
            return string_representation

    def distance(self, other):
            dx = self.x - other.x
            dy = self.y - other.y
            distance = math.sqrt(dx**2 + dy**2)
            return distance

# vector sub class
class Vector(Point):
    # override __str__ and + operator
    def __str__(self):
        other_string = f"Vector({self.x}, {self.y})"
        return other_string

    # instane method
    def add(self, other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y
        return Vector(new_x, new_y)

    def __add__(self, other):
        other_add = Vector(self.x + other.x, self.y + other.y)
        return other_add

# testing
point1 = Point(2, 4)
point2 = Point(8, 12) 

print("Points:")
print(point1)
print(point2)
print("Are points equals?", point1 == point2)
print("Distance between points:", point1.distance(point2))


# vetors
vector1 = Vector(1, 2)
vector2 = Vector(5, 8)

print("Vectors:")
print(vector1)
print(vector2)
print("Are points equals?", vector1 == vector2)
print("Are points equals?", vector1 == Vector(1, 2))
print("Distance between points:", vector1.distance(vector2))
print("Vector using add() method:", vector1.add(vector2))
print("Vector using + operator:", vector1 + vector2)