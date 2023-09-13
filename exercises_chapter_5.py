"""Here's are the points and exercises of chapter 5 of Python for Linguists book."""

# %%


# a function to print that sentence
def my___func():
    print("Colorless green ideas...")
    print("...sleep furiously")


my___func()  # invoke the function #collect the number
num = input("Enter a number: ")
# check if the number is < 5
if int(num) < 5:
    myfunc()  # print sentence again if so
else:
    print("Your number was big enough")


# %%


def myfunc():
    """This function checks whether your words is too long or not."""
    word = input("Word: ")
    print("This is your word:", word)
    if len(word) > 5:
        print("Your word was long.")
    else:
        print("Your word was short.")


myfunc()  # invoke function

# %%


def this_function():
    print("This prints:")
    return 6
    print("This doesn't print.")


x = this_function

print("Here's the function output: ", x)

# %%


def myfunc():  # function definition #collect two strings
    x = input("First string: ")
    y = input("Second string: ")
    z = x + " " + y  # concatenate strings #return all three
    return len(x), len(y), z


a, b, c = myfunc()  # 3 return values
print("a =", a)  # print the 3 values
print("b =", b)
print("c =", c)
# %%

# Functions that take arguments:


def myfunc(a, b):
    # return the concatenation #OR addition of those values
    return a + b


# invoke the function with numbers
print(myfunc(45, 10))
# invoke the function with strings
print(myfunc("strings ", "too"))

# %%

x = "a value"


def anotherfunc(a):
    a = "another value!"
    return a


print(x)
print(anotherfunc(x))
print(x)

# %%


x = [4, 5, 6]


def anotherfunc(a):
    a.append(7)

    return a


print(x)
print(anotherfunc(x))
print(x)

# %%


# function with default for 2nd arg
def f(x, y="oops"):
    return x + " " + y


print(f("hat"))  # invoked 3 ways
print(f(x="chair"))
print(f("hat", "chair"))
print(f(y="this", x="those"))

# %%


# function with unspecified #number of unnamed and named arguments
def func(*args, **kwargs):
    """This function takes unspecified number of unnamed arguments as a list in args
    and also takes unspecified number of named arguments as a dictionary in kwargs."""

    for a in args:  # print unnamed args
        print(a)

    for k in kwargs:  # print named args
        print(k, "\t", kwargs[k])

    # for k, kwargs in kwargs.items():  # print named args
    #     print(k, "\t", kwargs)


# invoked with unnamed FOLLOWED by #named arguments
func(3, 6, 8, hat="wow", chair=3.5, lamp="dark")

# %%


# Recursive and Lambda Functions


# function with 2 args: # a function f # and something else x
def func(f, x):
    return f(x)


print(func(len, "hat"))  # invoking it

# %%
