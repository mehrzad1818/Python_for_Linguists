"""
Write commands that print out your first name,
the number of characters in that name,
your last name, the number of characters in that name,
and then concatenate and print the two names (with a space).
"""

#%%
# 1.1
print("Mehrzad")
print("Mehrzad Barzegar")
print("Mehrzad" + "Barzegar")
print("Mehrzad" + " " + "Barzegar")

print(len("Mehrzad"))
print(len("Mehrzad Barzegar"))
print(len("Mehrzad" + "Barzegar"))
print(len("Mehrzad" + " " + "Barzegar"))

#%%
# 1.2
print("Write a line of code that will calculate how many \
       times the string ‘at’ occurs in this sentence.".count("at"))

#%%
# 1.3

print("This is Mike.".lower().upper())
print("This is Mike.".upper().lower())

# Answer: The last intended methods are always applied,
# We can clearly see that the method on the rightest
# most corner is applied to the string.

#%%
# 1.4

# Why does upper('This is a cat') not work?

# Answer: Because instances of methods are different
# from functions. They should come at the end of the argument.

#%%
# 1.5

# What does help(help) do in the interactive environment?

# Answer: Let's see it for ourselves.

help(help)

# Though help() itself is used for getting info about
# python objects, when we pass help into help it is evident
# that it gives information about object help itself.

# %%
# 1.6

# We used the mathematical operator ** on page 3 above without explanation.
# Play around with it and say what it does.

print(3 ** 12)
print(pow(3, 12))

# Answer: Double stars show power operator.
# One can also call pow() function to use it.

# %%
# 1.7

# In math, 6 + 2 and 2 + 6 mean the same thing.
# We’ve seen that + and * can be used with strings too.
# What happens if arguments are reversed when strings are involved?
# Do those expressions mean the same thing?

print(6 + 2)
print(2 + 6)
print(4 * 8)
print(8 * 4)

# print(6 + "Stanza") # Error
# print(2 + "5") # Error
print(6 * "Stanza")
print(type(2 * "5"))

# %%
# 1.8

# Use the help() function to find out about the round() command.
# Explain and demonstrate how to use it with more than one argument to produce different results.

print(help(round))

print(round( 45.2384923, 4))
print(round(43.251, 1))
print(round(43.250, 1))

# %%
# 1.9

# For each of the following, explain whether it’s true or false and why:

# (a) 'hat' == "hat"
# (b) hat == 'hat'
# (c) 1/3 == .33
# (d) 'three' > 'two'
# (e) 2 + 2 = 4

# Answer:

# a: There is not difference between double quotes and single quotes.
#    So, the expression "hat" == 'hat' is identical.

# b: This one is also correct, since the string is assigned to object hat.

# c: This one is wrong. Becuase 1/3 is continous, but .33 is not continuous.

# d: This one is false. Irregarding the string length, since strings are sequencable
#    and both starts with "t", while the second character is w, which has more value in the
#    memory compared to "h".

# e: It's wrong, since assignment takes place on the right side of the equal sign.

#%%
