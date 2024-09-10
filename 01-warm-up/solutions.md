1. Print out your name.

```py
print("Avery")
```

2. Store your name in a variable and print it out.

```py
name = "Avery"
print(name)
```

3. Get a name as input and print out "Hello (name)".

```py
name = input("Enter your name: ")
print("Hello", name)
```

Or

```py
name = input("Enter your name: ")
print("Hello " + name)
```

Or

```py
name = input("Enter your name: ")
print(f"Hello {name}")
```

4. Get a number as input and print out "positive", "negative", or "zero" depending on the sign of the number.

```py
num = float(input("Enter a number: "))

if n > 0:
   print("positive")
elif n < 0:
   print("negative")
else:
   print("zero")
```

5. Get two numbers as input. Print "ok" if one of the numbers is odd (but not both). Print "nope" otherwise.

```py
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# lots of possible ways to do this, but here's one solution

if a % 2 == b % 2:
   print("ok")
else:
   print("nope")
```
