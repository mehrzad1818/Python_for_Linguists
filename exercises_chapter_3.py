# Control Structures

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

if 3 - 1 > -3:
print("You are right.")

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
    print('or this....')
if 2 + 2 == 5:  # 1-statement block
    print("that shouldn't happen")
print('or this....')


# %%

# if and else clause:

if 2 + 2 == 5:
    print("this won't print")
else:
    print('but this will')
    print('...and so will this')
# %%

# Using pass in if block
# We can use pass to have an empty conditional expression.

x = 'hat'
if x[0] == 'h':
    pass
else:
    print('doing something here....')


# %%
# Advanced Printing

print("This is to test the print built-in function.")

print("This is the first file.", "This is the second file.",
      "This is the third file.", "", sep = "333")



# %%
