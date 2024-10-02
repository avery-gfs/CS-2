java mutable vs immutable
clone, copy
reverse for loop

immutable time
more methods
more classes
mutable classes: to-do list

what is self
mutable vs immutable
init args edit example
fix
don't update
fields def
init and repr description
how to call methods
how to make instances
multiple args

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

class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __repr__(self):
        return f"{self.feet}'{self.inches}\""

    def addInches(self, i):
        newInches = self.inches + i
        newFeet = self.feet

        if newInches >= 12:
            newInches -= 12
            newFeet += 1

        return Height(newFeet, newInches)

h = Height(5, 11)
print(h.addInches(4))

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

## Classes

----

## Review

#### Topics

- Repl
- Printing and user input
- Primitives: booleans, numbers (ints and floats), strings, `none`
- Type conversions
- Variable names
- Numerical operators
- Compound operators
- Boolean operators
- Comparison operators
- String addition and format strings
- Conditionals, nested conditionals
- For and while loops
- Functions: arguments, arity, side-effects, return values, early return
- Variable scope
- Lists: indexing, negative indexing, slicing, length, `append`, `reverse`, `sort`
- String `split` and `join`
- Tuples and destructuring
- Files: reading and writing
- Random numbers

#### Practice

***To do***: reformat practice problems, add test cases, solutions

[practice/review/practice.py](practice/review/practice.py)

----

## Links

[Python tutorial](https://docs.python.org/3/tutorial/index.html)

[Python library docs](https://docs.python.org/3/library/index.html)

[Python textbook](https://runestone.academy/ns/books/published/fopp/index.html?mode=browsing)
