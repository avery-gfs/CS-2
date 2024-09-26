## Topics

- **Objects**: Structures that combine data and functionality (methods).

- **Methods**: Functions that are attached to a value (like `.append()` for lists or `.lower()` for strings).

- **Classes** and **Instances**: A "class" is the category that an object belongs to. An object is an "instance" of a class if the object belongs to that class category. For example, the list object `["a", "b]` is an instance of class `list`.

- **Fields** or **Elements**: These names refer to data that is stored inside an object (for example items in a list).

```py
l = [1, 2, 3, 4]    # l is an object (an instance of class list)
print([0])          # we use the bracket syntax to get elements from a list
l.append(5)         # append is method that updates a list object
isinstance(l, list) # true
isinstance(l, int)  # false
```

- `self` parameter

- `__init__` method

- `__repr__` method

- Custom methods

## Making Classes

```py
import math

class Point:
  def __init__(self, x, y): # __init__ defines how a new point is created
    self.x = x # store x as a field on the new Point object 
    self.y = y # store y as a field on the new Point object

  def __repr__(self): # __repr__
    return f"Point({self.x}, {self.y})"

  def distanceTo(self, other): # custom method
    # calculates the distance between self and other
    dx = self.x - other.x # calc difference between x of self and other
    dy = self.y - other.y # calc difference between y of self and other
    return math.sqrt(dx ** 2 + dy ** 2) # distance formula

p = Point(3, 4)

p   # "Point(3, 4)"
p.x # 3
p.y # 4

o = Point(0, 0)
p.distanceTo(o) # 5

```
