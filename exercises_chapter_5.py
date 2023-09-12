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
