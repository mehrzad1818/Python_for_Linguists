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
print("Write a line of code that will calculate how many times the string ‘at’ occurs in this sentence.".count("at"))

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


