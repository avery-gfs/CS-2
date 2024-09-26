## Warm Up

Write a function that calculates the greatest common denominator of two integers.

## What are Objects?

- Data
- Functionality
- Identity
- Heirarchy

```py
l = [1, 2, 3, 4]
print([0])
l.append(5)
```

```py
print(isinstance(False, bool))
print(isinstance(False, int))
print(True + 1)
```

## Types of Functionality

- *Constructor* methods and *factory* methods make an object from scratch.
- *Transformer* methods make an object from an old object.
- *Mutator* methods update and object.
- *Observer* methods read or calculate data from an object.

## Making Classes

```py
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distanceTo(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    return math.sqrt(dx ** 2 + dy ** 2)

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2

  def slope(self):
    rise = self.p2.y - self.p1.y
    run = self.p2.x - self.p1.x
    return rise / run

  def midpoint(self):
    mx = (self.p1.x + self.p2.x) / 2
    my = (self.p1.y + self.p2.y) / 2
    return Point(mx, my)

  def length(self):
    return self.p1.distanceTo(self.p2)

  def __repr__(self):
    return f"Line({self.p1}, {self.p2})"
```
