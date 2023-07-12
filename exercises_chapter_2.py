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



x = True
y = False
C = x and y

print(C)

D = y or (not y)

print(D)


#%%

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


multi_line = """This is
an example 
of  multi-line string.
"""

x = '''This is
more than 
one line'''

print(x)

# Just like \n which gives us a new line, we can use \t to get tab.

print("What\tIs\tThis\tSorcery?\nWho\tThought\tYou\tThis?")

# Just like f-strings, we also have r-strings. They are used for 
# raw string notation. 

FORMULA = r"What\this\help\wai+t?"
print(FORMULA)

#%%
# Slots and format() method

TEMPLATE = '{Hey} Jimmy, {How} are you {doing}?'

TEMPLATE.format(Hey='Chitori',doing='What', How="Shit")


# %%

x = 'one = {1}; two = {0}'
x.format('dos','uno')

x = 'one = {uno}; two = {dos}'
x.format(dos='dau',uno='un')
x.format(uno='un',dos='dau')

# %%
# Advanced format() method

x = "What {:^18} Fuck"
x.format("the")

x = "What {:>13} Fuck"
x.format("the")

y = 4 * "This {2:<5} be a {1:^10} {0:>15} Unicorn."
y.format("might", "large", "hairy")

# %%
# String Extraction (Slicing)

names = "This is just a test."
names[-1]
names[len(names) - 1]

names[2:20:2]


# Thus x[n:n+1] is the same as x[n].
# If we have x[n:m] where m < n+1, we end up with an empty string.
# For example:
x = 'abcde'
x[2:2] # ''
x[2:1] # ''

# %%
# Lists

x = [1,6,4,9]
y = ['stops','fricatives','glides']
z = [7,'hats',56,'chairs',6.802]

len(x)
len(y)
len(z)

x[1]    # 6
y[0]    # 'stops'
z[3:]   # ['chairs',6.802]


# .append() method adds an element to the end of a list
x = ['rocks','paper']
x.append('scissors')
x

# y = "Thisisjustthe beginning."
# y.append("....")
# y ---------> You can't append to string. As it is not subscriptable.


# Next method is pop(). It takes index as input and removes the item, returning the value in the given index.

x = ['stops','fricatives','glides']
x.pop(1)

# The mirror method is insert(), it takes a value and an index, inserting it at the given value.

x = ['stops','fricatives','glides']
x.insert(1,'hello!')

# range() is a function that produces values between the given input

x = list(range(2000, 50, -2))
print(x)

# We also have the sort() and reverse() methods.
# The first sorts a list, and the second reverses it.
# Note that sort() works only for a list of uniform objects that are, in fact, sortable.

x = [5,2,8,3]
x.sort()
x
x = [5,2,8,3]
x.reverse()
x


# in operator check whether something is in something else

x = [5,2,8,3] 
8 in x
7 in x


x = "This is John Green. Welcome to another episode of Crash Course Literature."
y = x.count("t")
print(y)
"come" in x


# %%

# Tuples

# fixed sequence
# similar to list
# once created, cannot be changed (without modification)
# members are seperated with commas

# Some examples of tuples:

x = () # Empty tuple
y = (7,'hat',8.2) # Tuple with 3 members
z = (3,) # Tuple with one member


# The len() function applies to tuples, and you can index tuples just like lists.

y = (7,'hat',8.2)
len(y)
y[2]

# The in operator applies to tuples, just as it does to lists:

x = (5,2,8,3)
8 in x
7 in x

# Finally, we can convert a list to a tuple with tuple(),
# or a tuple to a list with list():

x = [1,2,3]
y = tuple(x)

a = (1,2,3)
b = list(a)

#%%
# Dictionaries
