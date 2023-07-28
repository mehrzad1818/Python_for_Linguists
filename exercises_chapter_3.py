"""Control Structures"""

# if is the first control structure we're going to learn,
# it's basically used for conditional application,
# where a given test clause is followed by one or several block.
# based on the test clause's answer, the conditions are met.

# %%
# control1.py

if 2 + 2 == 4:
    print(f"The answer is {4}.")

# %%
# control2.py

# The code below produces error, since it's not indented.

# if 3 - 1 > -3:
# print("You are right.")

# %%
# control3.py

if isinstance(23, int):
    print("This is a number.")
    print("I'm sure it's a number.")
    print("Come on, dude!")
# %%
# control 6 and 7 .py
if 2 + 2 == 5:  # 2-statement block
    print("that shouldn't happen")
    print("or this....")
if 2 + 2 == 5:  # 1-statement block
    print("that shouldn't happen")
print("or this....")


# %%

# if and else clause:

if 2 + 2 == 5:
    print("this won't print")
else:
    print("but this will")
    print("...and so will this")
# %%

# Using pass in if block
# We can use pass to have an empty conditional expression.

x = "hat"
if x[0] == "h":
    pass
else:
    print("doing something here....")


# %%
# Advanced Printing

print("This is to test the print built-in function.")

# print function takes arguments: you can use sep to separate strings with the given argument.
# or you can use end to put something at the end of the print function.
print(
    "This is the first file.",
    "This is the second file.",
    "This is the third file.",
    sep="333",
    end="13242",
)

print("one", "two", "three", sep="-")

print("one", "two", "three", sep="")

# %%

# for control structure

the_list = [232, 1221, 12123, 1212, 3, 23, 123, 12, 312, 3]
for names in the_list:
    print(names)

# we don't need to use each values held by the 'names' here:

numbers = [23, 123, 123, 123, 123, 123, 123, 3, 4, 5345, 34, 34, 534]

for num in numbers:
    print(f"Hey{'':>10}, This is the number: {num:>13}")


# nothing prevents us from using the variable more than once per each iteration.

for i in [1, 2, 3]:
    print("{} + 2 = {}".format(i, i + 2))


num1 = [12, 23, 234, 354524]
num2 = 123

for x in num1:
    print(f"{x:>12} + 123 = {x + num2}")


# we can use "for" to iterate over strings, too.

for i in "tone":
    print(i, end=" + ")


# we can combine for and range to count and iterate over a list of numbers:

variable = 0

for number in range(0, 101):
    variable += number
print(variable)

# %%
# for, range, and recursion mixed:

words = ["feminism", "communism", "socialism", "capitalism"]

for word in words:
    print(word)
    for number in range(4):
        word = "anti-" + word
        print(word)


# %%

# define prefix and 3 words

prefix = "anti"
words = ["missile", "racism", "music"]

for word in words:
    print(word)
    for i in range(3):
        word = prefix + "-" + word
        print(word)

# %%

total = 0
for number in range(10001):
    total += number
print(total)

# %%

# Write a code to count vowels in a string.


vowels = "aeiou"

sentence = """
This is an example of a sentence that
we are going to test how
many vowels does it have
"""

vowelcount = 0

for letter in sentence:
    if letter in vowels:
        vowelcount += 1
print(vowelcount)

####


vowels = "aeiou"
letterCount = 0
word = "Appalachicola"

if word[0].lower() in vowels:
    for letter in word:
        letterCount += 1
else:
    print("Not vowel-initial")
print(letterCount)

# %%
# while loop


y = 12
x = 13

while x == y:
    print("We're good.")


# same program with while and for:

count = 0
while count < 5:
    count += 1
    print(count)

for number in range(1, 6):
    print(number)

# %%
# two while loops nested

word = "accumulation"
count = 0

while count < len(word):
    print(word[count])
    count += 1
    other_count = 1

    while other_count < count + 1:
        print("\t", word[0:other_count])
        other_count += 1


# %%
# if and while nested
# This program checks a word against a list.
# The output is the letters that weren't in the list.

word = "alphabet"
vowels = "aeiou"
count = 0

while count < len(word):
    letter = word[count]
    if letter not in vowels:
        print(letter)
    count += 1

# %%

# While loop to for loop and vice versa.

for i in [1, 2, 3]:
    print(i)

for i in [1, 2, 3]:
    print(i)


number = 1
while number < 4:
    print(number)
    number += 1

# %%
# While loop has an else controller.

vowels = "aioue"
word = "thisiswhatithinkabout"

counter = 0
vowel_counter = 0

while counter < len(word):
    if word[counter] in vowels:
        vowel_counter += 1
    counter += 1
else:
    print(f"There are {vowel_counter} vowels in this word.")

# %%

# Break and Continue in While and If loop:

word = "sthenic"
vowels = "aeiou"
counter = 0

while counter < len(word):
    if word[counter] in vowels:
        break
    counter += 1

print("The word begins with", counter, "consonant letters")

word = "sthenic"
vowels = "aeiou"
counter = 0

for letter in word:
    if letter in vowels:
        break
    counter += 1

print("The word begins with", counter, "consonant letters")

# %%
"""This is a playground to test my codes."""

COMMAND = ""

while COMMAND.lower() != "quit":
    COMMAND = input("> ")
    print("ECHO", COMMAND)

while True:
    COMMAND = input("> ")
    print("ECHO", COMMAND)
    if COMMAND.lower() == "quit":
        break


count = 0
start = int(input("What is your starting number?\n"))
end = int(input("What is your finishing number?\n"))

for number in range(start, end):
    if (number % 2) == 0:
        print(number)
        count += 1
print(f"You have {count} even numbers.")


"""This is a playground to test my codes."""


# We have two types of functions: 1. Performs a task
def greeting(first_name, last_name):
    """Welcomes the people."""
    print(f"Hi {first_name} {last_name}.")
    print("How are you today?")


name = input(f"What's your name?\n{'':<2}").title()
last = input(f"What's your last name?\n{'':<2}").title()

greeting(name, last)


# We have two types of functions: 2. Returns a value
def greeting_2(first_name):
    """It welcomes people, but more efficiently."""
    return f"Hi, {first_name}."


print(greeting_2(first_name="Mick"))


def increment(number, by_degree=3):
    """Adds two values together."""
    return number + by_degree


print(increment(2))


"""This is a playground to test my codes."""


# def increment(number, another, by_degree=3):
#     """Adds two values together."""
#     return number + by_degree + another


# print(increment(23, by_degree=12, another=62))


def multiply(*numbers):
    """Multiplies given numbers."""
    total = 1
    for number in numbers:
        total *= number
    return f"The total is: {total}"


print(multiply(12, 42, 32, 1, 1, 3))


def mus(*numbers):
    """Sums given numbers."""
    total = 0
    for number in numbers:
        total += number
    return f"The total is: {total}"


print(mus(12, 42, 32, 1, 1, 3))


"""This is a playground to test my codes."""


def save_user(**user):
    """Saves the info inside a dictionary."""
    print(user)


save_user(id=(1, 2, 3, 4), name=("John", "James", "Jane", "Joan"), age=(18, 22, 17, 16))


# These are instance of local scop
def greet(name):
    """Greets people."""
    message = "a"
    print(message, name)


# # Here, the scope of message is global.
message = "b"


def send_email(name):
    """Sends an email."""
    global message
    message == 1
    print(message, name)


# You can use global keyword to define and modify a variable, but the problem
# is that it will cause bugs and errors most of the time.


def multiply(*numbers):
    """It multiplies."""
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 6, 345, 34, 523, 467, 56, 3, 35, 34, 34))


def fizz_buzz(your_guess):
    """Plays the game."""

    if (your_guess % 5 == 0) and (your_guess % 3 == 0):
        return "FizzFuzz"

    elif your_guess % 5 == 0:
        return "Fuzz"

    elif your_guess % 3 == 0:
        return "Fizz"

    else:
        return your_guess


print(fizz_buzz(int(input("What's your number?"))))


# %%
# try exception (error management)


lst = [1, 2.2, 3, True, "Hello", [1, 2], (1, 43), 234, 4635]

for i in lst:
    try:
        print(i**2)
    except:
        pass


while True:
    try:
        number = int(input("Enter a number: "))
        print(number**2)
        break
    except:
        print("Enter a valid number. (No extra characters)")

# %%

vowels = "aeiou"  # define vowels
word = "sthenic"  # define word
counter = 0  # initialize counter
# go through all letters
for i in range(len(word)):
    # is current letter a vowel?
    if word[i] in vowels:
        break  # if so, exit loop
    # don't forget to update counter
    counter += 1
# print result
print("The word begins with", counter, "consonant letters")

# %%


vowels = "aeiou"
word = "shgftheegtfnic"
counter = 0
for i, letter in enumerate(word):
    if letter not in vowels:
        counter += 1
print("The word begins with", counter, "consonant letters")

# %%


vowels = "aeiou"  # define vowels
word = "sthenic"  # define word
counter = 0  # initialize counter
# go through each letter
for i in range(len(word)):
    # is current letter a vowel?
    if word[i] in vowels:
        continue  # if so, skip it
    # increment counter (only for non-vowels!)
    counter += 1
# print result
print("The word has", counter, "consonant letters")

# %%


# CV Monosyllabic generator


vowels = "aiu"  # define vowels
consonants = "ptk"  # define consonants

for consonant in enumerate(consonants):
    for vowel in enumerate(vowels):
        CV = consonant + vowel
        print(consonant, vowel, sep="")

# %%


vowels = "aiu"
consonants = "ptk"

for v in vowels:
    for c in consonants:
        print(c, v, sep="")

# %%
# With more words, it becomes more relevant.

vowels = "aeiou"
consonants = "ptkbdg"

for v in vowels:
    for c in consonants:
        print(c, v, sep="")

# %%

# CVC syllables

vowels = "aeiou"
consonants = "ptkbdg"
add = 0

for v in vowels:
    for o in consonants:
        for c in consonants:
            print(o, v, c, sep="")
            add += 1
print(add)


# %%


"""Python is the best."""


letters = ["a", "b", "c"]
matrix = [[0, 1]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(21))
chars = list("Hello World")
print(len(chars))

# %%
# Part 2 - Accessing Items
letters = list("abcd")
# alphabet = set(list("thequickbrownfoxjumpsoverthelazydog"))
# print(len(alphabet))
letters[3] = "D"
print(letters)

print(letters[0:3:2])
print(letters[0::2])
print(letters[-1::-1])


new_numbers = list(range(21))

print(new_numbers[::2])
print(new_numbers[::-2])
print(new_numbers[::-1])
print(new_numbers[::1])

# %%
numbers = list(range(21))
first, second, third = numbers


first, second, *this = numbers


# What just happened above is just like what we did in multiply function:


def multiply(*numbers):
    """It multiplies."""
    total = 1
    for number in numbers:
        total *= number
    return total


print(
    multiply(
        5195154245245245245294851,
        418452424524245424125846,
        464642424524524552452542454,
        536344524524592452424524524563,
        23342422245245452523452345,
        234525424529542452453452345,
        232445254245524524524546,
        6452544522542542542452547,
        42452542452445245245524525,
        45645694524529252242542542465,
        7897842452452452425673423,
        2344524524525425245439992,
    )
)

print(first)
print(second)
print(this)

# The code above is the same as the code below.

first = numbers[0]
second = numbers[1]
third = numbers[2]


# %%
# Here we learn more new things about lists:


letters = ["a", "b", "c", "d", "e", 23, 46, True]

for index, letter in enumerate(letters):
    print(f"{index} {letter} {type(letter)}")

# %%

# append method is used to add items to the end of a list


letters = ["a", "b", "c"]

# Add

letters.append("d")
letters.insert(0, "-")


# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)


# %%
# Finding items:


letters = ["a", "b", "c"]
print(letters.count("d"))
print(letters.index("a"))
if "h" in letters:
    print(letters.index("h"))

# %%
# Sorting Lists


numbers = [23, 56, 1, 34, 87, 234]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print((numbers))


# the difference between sort method and sorted function is that
# the latter returns a new list with sorted items.

# How can we sort tuples???

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


def sort_item(item):
    """Makes items a list"""
    return item[1]


items.sort(key=sort_item)
print(items)


# There's a more efficient way for the above code.
# %%


# Lambda function
# lambda arguments : expression


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


items.sort(key=lambda item: item[1])
print(items)

# %%

# Mapping function (lambda)
# lambda arguments : expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


prices = []
for item in items:
    prices.append(item[1])

print(prices)

# This is one basic way of mapping data into a new data type.

# Below is the more advanced format:

prices = list(map(lambda item: item[1], items))
print(prices)

# %%
# Filter function
# lambda arguments : expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


overpriced = list(filter(lambda james: james[1] >= 10, items))
print(overpriced)

# %%


# List Comprehension
# [Expression for something in somethings]

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


prices = list(map(lambda item: item[1], items))
print(prices)
prices = [item[1] for item in items]
print(prices)


overpriced = list(filter(lambda james: james[1] >= 10, items))
print(overpriced)

overpriced = [item[1] >= 10 for item in items]
print(overpriced)

overpriced = [item for item in items if item[1] >= 10]
print(overpriced)

# %%

# Zip Function

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50, 60]


print(list(zip("abcdef", list1, list2)))

# %%

# Stack (Stack of items, LIFO)

# LIFO -> Last in - First out


browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])

if not browsing_session:
    print("disable")

# %%

# Queue

# FIFO -> First in First out

# from module import class

from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# %%

# Tuples
