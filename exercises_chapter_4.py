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

# This is a sample of importing and visualizing data from a file:

# import from scipy and matplotlib
import scipy.io.wavfile, matplotlib.pyplot

# read sample rate and wave vector from file
x, y = scipy.io.wavfile.read("mha.wav")
vdur = len(y) / x  # calculate duration #print duration
print("Duration of wave:", vdur)
matplotlib.pyplot.plot(y)  # make plot
matplotlib.pyplot.show()  # show plot

# %%


# This is an example of visualizing Excel data.

import openpyxl  # to handle xls/xlsx files

# read in data
wb = openpyxl.load_workbook("Classmates intel.xlsx", read_only=True)
# get the names of 'sheets'
print(wb.get_sheet_names())
# get the first sheet
sheet = wb["Classmates"]
# print contents of cell B2 on sheet1
print(sheet["B2"].value)
r = 0  # keep track of rows #go through all rows
for c in sheet.rows:
    print(r)  # print the row number #print cells in each row
    for i in range(len(c)):
        print("\t", c[i].value)
    r += 1

# %%

# App to do lexical statistics


count = 0  # counter for lines
f = open("bible.txt", "r", encoding="utf8")  # open the file
for line in f:  # read line by line
    count += 1
f.close()  # close file
print("lines:", count)  # print line count


# %%
# Save and store the contents of the bible

f = open("bible.txt", "r", encoding="utf8")

for line in f:
    count += 1
    lines.append(line)

f.close()

print("lines:", count)
print("saved lines:", len(lines))

# %%


count = 0
lines = []

f = open("bible.txt", "r", encoding="utf8")

for line in f:
    count += 1
    lines.append(line)

f.close()

i = 5000
while i < 6000:
    print(lines[i], end="")
    i += 1

print("lines:", count)
print("saved lines:", len(lines))

# %%


words = []  # list of all words
lines = []  # list of all lines
# open file
f = open("bible.txt", "r", encoding="utf8")


for line in f:  # save lines one by one
    lines.append(line)
f.close()  # close file


# go through lines one by one
for line in lines:
    # break each line into words
    wds = line.split()
    # add words to list
    words += wds

i = 50000
while i < 70000:
    # store the count for the current word
    count = 0
    # convert the current word to lowercase
    word = words[i].lower()
    # go through word letter by letter #if lowercase, add 1 to count
    for l in word:
        if l in "abcdefghijklmnopqrstuvwxyz":
            count += 1
    print(i, words[i], count)  # print it all
    i += 1
# %%


words = []  # list of all words
lines = []  # list of all lines
wordlengths = {}  # dictionary of word lengths

# open file
f = open("bible.txt", "r", encoding="utf8")
for line in f:  # save lines one by one
    lines.append(line)
f.close()  # close file


# go through the lines one by one
for line in lines:
    # break each line into words
    wds = line.split()
    # add the words to the list
    words += wds


for wd in words:
    count = 0  # count for current word #convert current word to lowercase
    word = wd.lower()
    # go through word letter by letter #if lowercase, add 1 to count
    for l in word:
        if l in "abcdefghijklmnopqrstuvwxyz":
            count += 1

    # check if we've seen this length before
    if count in wordlengths:
        # if so add 1
        wordlengths[count] += 1
    else:
        # if not, set to 1
        wordlengths[count] = 1


# print out counts for each word length
for k, v in wordlengths.items():
    print(k, v)

# %%


the_book = open("romeo.txt", mode="r", encoding="utf8")

the_book_lines = []

for each_line in the_book:
    the_book_lines.append(each_line)

the_book.close()

refined_the_book_lines = []

for this in the_book_lines:
    if this == "\n":
        continue
    refined_the_book_lines.append(this)
    # print(this, end="")


the_book_words = []

for words in refined_the_book_lines:
    words.split()
    the_book_words += words

print(the_book_words)

diction_book = {}

for word in the_book_words:
    if word in diction_book:
        diction_book[word] += 1
    else:
        diction_book[word] = 1

print(diction_book)

# %%


# Exercise 4.1
# 4.1 Tweak the io3.py program to accommodate uppercase vowels.

import sys  # make sys.argv available

vowels = "aeiou"  # define vowels

# iterate over all words in list
for word in sys.argv[1:]:
    counter = 0  # proceed as before
    vowelcount = 0

    while counter < len(word):
        if word[counter] in vowels:
            if word[counter] in "ABCDEFGHIJKLMNOPQRSTUWXYZ":
                vowelcount += 1
            counter += 1
    else:
        print("There are", vowelcount, "vowels in", word)

# %%

# 4.1 Consonant and Vowel counter

my_text = input("Paste a text here: ")

vowels = "aioueAIOUE"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
my_dict = {}
my_paradigms = ["vowel", "consonant", "uppercase", "lowercase"]

for paradigm in my_paradigms:
    my_dict[paradigm] = 0


for word in my_text.split():
    for letter in word:
        if letter.isalpha():
            if letter in vowels and letter.isupper():
                my_dict["vowel"] += 1
                my_dict["uppercase"] += 1

            if letter in vowels and letter.islower():
                my_dict["vowel"] += 1
                my_dict["lowercase"] += 1

            if letter in consonants and letter.isupper():
                my_dict["consonant"] += 1
                my_dict["uppercase"] += 1

            if letter in consonants and letter.islower():
                my_dict["consonant"] += 1
                my_dict["lowercase"] += 1


print(my_dict)

# %%


my_text = input("Paste a text here: ")

vowels = "aioueAIOUE"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
my_dict = {"vowel": 0, "consonant": 0, "uppercase": 0, "lowercase": 0}

for word in my_text.split():
    for letter in word:
        if letter.isalpha():
            if letter in vowels:
                my_dict["vowel"] += 1
            else:
                my_dict["consonant"] += 1

            if letter.isupper():
                my_dict["uppercase"] += 1
            else:
                my_dict["lowercase"] += 1

print(my_dict)
# %%


# 4.7 Write a program that takes a simple mathematical expression
# on the command line like '7 / 45', parses it correctly, and prints the result.


# %%

# 4.8 Write a program that goes through the Alice text and prints out all multiple
#  wh- questions. We define these as questions that begin with a wh- word
#  and contain at least one more wh- word in the question.
# (If you already know what they are, you may not use regular expressions.)


lines = []

f = open("bible.txt", "r", encoding="utf8")
for line in f:
    lines.append(line)
f.close()

wh_questions = [
    "what",
    "where",
    "why",
    "when",
    "which",
    "whose",
    "whom",
    "who",
    "how",
]


count_words = 0
count_lines = 0

for line in lines:
    count_lines += 1

    for wh_words in wh_questions:
        if wh_words in line:
            # print(line)
            count_words += 1

print(count_words)
print(count_lines)
# %%

# 4.9 Write a program that:
# (a) Reads in the Alice file;
# (b) strips off the header;
# (c) converts everything to lowercase;
# (d) converts all punctuation to spaces;
# (e) splits the text into words;
# (f) counts up how frequent all words are;
# (g) prints out the 10 most frequent words and their counts.


lines_of_bible = []


opened_book = open("bible.txt", mode="r", encoding="utf8")
for each_line in opened_book:
    lines_of_bible.append(each_line)
opened_book.close()


for line in lines_of_bible:
    for word in line:
        print(word)

# %%
