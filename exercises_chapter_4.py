
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
