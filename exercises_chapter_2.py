# print(help(False))
# print(help(class))
# print(help(finally))
# print(help(is))
# print(help(return))
# print(help(None))
# print(help(continue))
# print(help(for))
# print(help(lambda))
# print(help(try))
# print(help(True))
# print(help(def))
# print(help(from))
# print(help(nonlocal))
# print(help(while))
# print(help(and))
# print(help(del))
# print(help(global))
# print(help(not))
# print(help(with))
# print(help(as))
# print(help(elif))
# print(help(if))
# print(help(or))
# print(help(yield))
# print(help(assert))
# print(help(else))
# print(help(import))
# print(help(pass))
# print(help(break))
# print(help(except))
# print(help(in))
# print(help(raise))


# Above are the examples of Python reserved words.


# Logical Operators (and, or, not) and Booleans (True, False)

X = True and False
Y = not (False or False)
Z = not (not True)

print(X, Y, Z)


A = not (False or True)
B = (not False) or True

print(A, B)


X = True
Y = False
C = X and Y

print(C)

D = Y or (not Y)

print(D)


# %%

# Comparison              Example

# equality                3 == 2 + 1
# inequality              7 != 2
# greater than            5 > 3
# greater than or equal   5 >= 5
# less than               2 < 7
# less than or equal      5 + 6 <= 10 * 3


# Comparison                              Example

# equality                                'hat' == 'hat'
# inequality                              'hat' != 'cat'
# follows alphabetically                  'hat' > 'cat'
# follows alphabetically or equal         'Hat' >= 'hat'
# precedes alphabetically                 'Hat' < 'hat'
# precedes alphabetically or equal        'hat' + 's' <= 'chair'


# There are two ways which we can test the type of elements:

# One is to use type() function:
type("What is the type of me?")
type(2342.2342)

# Second is to use isinstance(), which is a boolean version of type() function:
isinstance(23, float)
isinstance("What is this?", str)


MULTI_LINE = """This is
an example
of  multi-line string.
"""

X = """
This is
more than
one line
"""

print(X)

# Just like \n which gives us a new line, we can use \t to get tab.

print("What\tIs\tThis\tSorcery?\nWho\tThought\tYou\tThis?")

# Just like f-strings, we also have r-strings. They are used for
# raw string notation.

FORMULA = r"What\this\help\wai+t?"
print(FORMULA)

# %%
# Slots and format() method

TEMPLATE = "{Hey} Jimmy, {How} are you {doing}?"

TEMPLATE.format(Hey="Woozy", doing="What", How="Shit")


# %%

X = "one = {1}; two = {0}"
X.format("dos", "uno")

X = "one = {uno}; two = {dos}"
X.format(dos="dau", uno="un")
X.format(uno="un", dos="dau")

# %%
# Advanced format() method

X = "What {:^18} Fuck"
X.format("the")

X = "What {:>13} Fuck"
X.format("the")

Y = 4 * "This {2:<5} be a {1:^10} {0:>15} Unicorn."
Y.format("might", "large", "hairy")

# %%
# String Extraction (Slicing)

NAMES = "This is just a test."
print(NAMES[-1])
print(NAMES[len(NAMES) - 1])
print(NAMES[2:20:2])


# Thus x[n:n+1] is the same as x[n].
# If we have x[n:m] where m < n+1, we end up with an empty string.
# For example:
X = "abcde"
print(X[2:2])  # ''
print(X[2:1])  # ''

# %%
# Lists

x = [1, 6, 4, 9]
y = ["stops", "fricatives", "glides"]
z = [7, "hats", 56, "chairs", 6.802]

len(x)
len(y)
len(z)

print(x[1])  # 6
print(y[0])  # 'stops'
print(z[3:])  # ['chairs',6.802]


# .append() method adds an element to the end of a list
x = ["rocks", "paper"]
print(x.append("scissors"))

# y = "Thisisjustthe beginning."
# y.append("....")
# y ---------> You can't append to string. As it is not subscriptable.


# Next method is pop(). It takes index as input and removes the item,
# returning the value in the given index.

x = ["stops", "fricatives", "glides"]
x.pop(1)

# The mirror method is insert(), it takes a value and an index,
# inserting it at the given value.

x = ["stops", "fricatives", "glides"]
x.insert(1, "hello!")

# range() is a function that produces values between the given input

x = list(range(2000, 50, -2))
print(x)

# We also have the sort() and reverse() methods.
# The first sorts a list, and the second reverses it.
# Note that sort() works only for a list of uniform objects that are sortable.

x = [5, 2, 8, 3]
print(x.sort())

x = [5, 2, 8, 3]
print(x.reverse())


# in operator check whether something is in something else

x = [5, 2, 8, 3]
print(8 in x)
print(7 in x)


X = "This is John Green. Welcome to this episode of Crash Course Literature."
Y = X.count("t")
print(Y)
print("come" in x)


# %%

# Tuples

# fixed sequence
# similar to list
# once created, cannot be changed (without modification)
# members are separated with commas

# Some examples of tuples:

x = ()  # Empty tuple
y = (7, "hat", 8.2)  # Tuple with 3 members
z = (3,)  # Tuple with one member


# The len() function applies to tuples,
# and you can index tuples just like lists.

y = (7, "hat", 8.2)
len(y)
print(y[2])

# The in operator applies to tuples, just as it does to lists:

x = (5, 2, 8, 3)
print(8 in x)
print(7 in x)

# Finally, we can convert a list to a tuple with tuple(),
# or a tuple to a list with list():

x = [1, 2, 3]
y = tuple(x)

a = (1, 2, 3)
b = list(a)

# %%
# Dictionaries


# sets of pairs
# first element used to “look up” the second element
# first element  must  be distinct from the
# first elements of all the other pairs.
# curly brackets within which each pair of elements is separated with a colon.

# For example:

d = {"cat": 7, "chair": "hat", "table": 7}

# dictionary = {key1:value1, key2:value2, key3:value3}

# look up values by putting the key in square brackets
# after the name of the dictionary


d = {"cat": 7, "chair": "hat", "table": 7}
print(d["cat"])
print(d["chair"])

# len() is applicable to dicts, they return number of pairs.

print(len(d))


d = {"cat": 7, "chair": "hat", "table": 7}
d["onion"] = 3.7
print(d)
print(len(d))


# WE can check whether specific key is in the dict,
# notice we can't to this with value, only the key.

print("cat" in d)


# Dictionary items can be altered or deleted.
d = {"cat": 7, "chair": "hat", "table": 7}
d["cat"] = d["cat"] + 2
print(d["cat"])
del d["cat"]


# Keys, values, or key-value pairs can be extracted:

d = {"cat": 7, "chair": "hat", "table": 7}

# the type of output of these file are unique:

print(type(d.keys()))
print(type(d.values()))
print(type(d.items()))

print(d.keys())  # We access keys (unique, first)
print(d.values())  # We access value (not unique, second ...)
print(d.items())  # Both keys and value (unique)

# Use format() with dictionaries.

# special operator for this **
# basic idea is that the slots in the
# string are named. The values that go
# in those slots are associated with the relevant keys of the dictionary

D = {"uno": "eins", "dos": "zwei", "tres": "drei"}
S = "one = {uno} and three = {tres}"
S.format(**d)

# %%
# Mutability

d = {"un": "un", "deux": "?", "trois": "tri"}
d["quatre"] = "pedwar"
d["deux"] = "dau"

# Garbage Collection

# This concept revolves around removing un-necessary information in the memory.
# When we assign i = 8 and then, i = 12, the value of i is 12, not 8.
# Mutable elements, such as dictionaries and lists can be directly changed.

x = ["Tom", "Dick", "Harry"]
x[1] = "Mary"  # Inserts "Mary" with whatever is at index 1, which is "Dick".

x.append("Edna")  # append() adds Edna to the end of the list.


# Dictionaries are mutable, too.

d = {"un": "un", "deux": "?", "trois": "tri"}
d["quatre"] = "pedwar"  # Adds a new key-value to the dict
d["deux"] = "dau"  # Finds the key deux, and assigns value dau to it.


X = 3
X = 7
# the output would be 7
# (mutability and garbage collection are intertwined somehow.)

Y = True
Y = False
# Again, output would be False, not True.

# Tuples and Strings are not mutable.
# We can't directly modify them.
# Assigning a new value to the same object is not considered mutability.
