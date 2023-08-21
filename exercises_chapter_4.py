"""This file includes exercises from Chapter 4 of Python for Linguists book."""
# %%

# Input_Output

import sys

print(sys.argv)


# %%


# We can use this mechanism to make our vowel-counting program
# completely flexible. Recall the vowel-counting program
# control32.py on page 45, repeated below


vowels = "aeiou"  # define vowels
word = "Winnepesaukee"  # set word

# create two counters
counter = 0
vowelcount = 0

# go letter by letter
while counter < len(word):
    # is current letter a vowel?
    if word[counter] in vowels:
        vowelcount += 1
    # keep track of total number of letters
    counter += 1
    # when counter is too big, do this:
else:
    print("There are", vowelcount, "vowels in this word")


# %%

# We can minimally revise this program as follows so that
#  the relevant word comes from the command line:

import sys  # make sys.argv available

vowels = "aeiou"  # define vowels
word = sys.argv[1]  # get word from command-line
counter = 0  # proceed as before...
vowelcount = 0

while counter < len(word):
    if word[counter] in vowels:
        vowelcount += 1
    counter += 1
else:
    print("There are", vowelcount, "vowels in this word")

# %%

import sys

for line in sys.stdin:
    print(line)

# %%

# echo hat | testing.py

# In this way, we can pipe down inputs to our program.

# %%

# Program 5


import sys

# the line which should be put in the command line for this code is

# echo <Your text> | python <the address of the file with .py>

vowels = "aeiou"

for words in sys.stdin:
    for word in words.split():
        counter = 0
        vowelcount = 0

        while counter < len(word):
            if word[counter] in vowels:
                vowelcount += 1
            counter += 1
        else:
            print("There are", vowelcount, "vowels in", word)


# %%


import sys


vowels = "aioue"
line = 1

for words in sys.stdin:
    print("This is line", line)
    line += 1

    for word in words.split():
        counter = 0
        vowel_count = 0

        while counter < len(word):
            if word[counter] in vowels:
                vowel_count += 1
            counter += 1
        else:
            print("\t There are", vowel_count, " vowels in ", '"', word, '"', sep="")


# %%


# In this method we can feed several lines of a file into this program

# Use the command line below:

# """
# type <text file name in .txt format> | python <name of the program in .py>
# """


import sys


vowels = "aioue"
line = 1

for words in sys.stdin:
    print("This is line", line)
    line += 1

    for word in words.split():
        counter = 0
        vowel_count = 0

        while counter < len(word):
            if word[counter] in vowels:
                vowel_count += 1
            counter += 1
        else:
            print("\t There are", vowel_count, " vowels in ", '"', word, '"', sep="")

sys.stdout


# %%

import random

letters = "abcdefghijklmnopqrstuvwxyz"
letter = letters[random.randint(0, 25)]


while True:
    guess = input("Type a lower-case letter: ")

    if guess not in letters:
        print("That's not a lower-case letter.")
        continue
    if guess == letter:
        print("That's right!")
        break
    if guess > letter:
        print("It's earlier in the alphabet.")
    else:
        print("It's later in the alphabet.")


# %%

# not what we want!

x = "Tom"
y = "Dick"
z = "Harry"

result = input("Type x, y, or z: ")
print(result)

# %%

# set up three variables
x = "Tom"
y = "Dick"
z = "Harry"
# collect user input
result = input("Type x, y, or z: ")
# evaluate and print result
print(eval(result))

# %%


# open file stream
outFile = open("testfile.txt", mode="w")
# write to it
outFile.write("some some some some text!\n")
outFile.write("...and some some some some some more text!\n")
outFile.close()  # close file stream

# %%


inFile = open("testfile.txt", mode="r")
stuff = inFile.read()
inFile.close()

print(stuff)

# %%

# open file
inFile = open("testfile.txt", "r")
stuff = inFile.read()  # read file contents
inFile.close()  # close file
lines = stuff.split("\n")  # split into lines
# print lines and lengths
for line in lines:
    print(len(line), ": ", line, sep="")

# %%

# open file
inFile = open("testfile.txt", "r")
# read from stream line by line
for line in inFile:
    # print length of line and the line
    print(len(line), ": ", line, sep="", end="")
inFile.close()  # close file stream

# %%
