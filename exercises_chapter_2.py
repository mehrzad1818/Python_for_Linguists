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

y = 4 * "This {0:<5} be a {1:^10} {2:>15} Unicorn."
y.format("might", "large", "hairy")
# %%
