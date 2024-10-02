# TO DO: reformat as problems, add test cases

# Printing: Print out your name

print("Avery")

# Variables: Store your name in a variable and print it out

name = "Avery"
print(name)

# Input: Get a name as input and print out "Hello (name)"

name = input("Enter your name: ")
print("Hello", name)

# or

name = input("Enter your name: ")
print("Hello " + name)

# or

name = input("Enter your name: ")
print(f"Hello {name}")

# Conditionals: Get a number as input and print out "positive", "negative", or "zero" depending on the sign of the number

num = float(input("Enter a number: "))

if num > 0:
   print("positive")
elif num < 0:
   print("negative")
else:
   print("zero")

# Logic: Get two numbers as input. Print "ok" if one of the numbers is odd (but not both). Print "nope" otherwise

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# lots of possible ways to do this, but here's one solution

if a % 2 != b % 2:
   print("ok")
else:
   print("nope")

# **Palindrome Finder**: Download and save the `unixdict.txt` file. Write a program to read the words in the file and find the palindromes (words that are the same in reverse as forwards). Find the longest palindrome in the file.

# **Anagram Finder**: Write a program that takes a word as input and finds all of the anagrams (from `unixdict.txt`) of the input word. Words are anagrams of each other if they contains the same letters in a different order. For example, the anagrams of `time` are `mite`, `emit`, and `item`. Find the largest set of anagrams in the file.

# **Day Calculator**: Get a string `startDay` and a number `n` as input, print out what the day of the week it will be `n` days from `startDay`.

# **Change Calculator**: Get a number `n` as input. Calculate the "change" for `n`; that is, the smallest set of quarters, dimes, nickles, and pennies to make `n` cents.

