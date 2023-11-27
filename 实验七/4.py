import math

class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return '(' + ','.join(str(x) for x in self.vector) + ')'

    def equals(self, other):
        return self.vector == other.vector

    def add(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same length")
        result = [a + b for a, b in zip(self.vector, other.vector)]
        return Vector(result)

    def subtract(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same length")
        result = [a - b for a, b in zip(self.vector, other.vector)]
        return Vector(result)

    def dot(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same length")
        result = sum(a * b for a, b in zip(self.vector, other.vector))
        return result

    def norm(self):
        result = math.sqrt(sum(x ** 2 for x in self.vector))
        return result