# print() function outputs on the screen the inputted string
print("Welcome to my first python program\n")

# input() function prompts the user to enter a value
f_name = input("Please enter your first name:\n")
l_name = input("Please enter your last name:\n")

# outputting a hello message with the full name of the user
print("\nHello", f_name, l_name, "!\n")

# variables used to store data about a movie with different data types
# variable names in python are usually written in snake_form (Lcase with underscores)
movie_name = "world war z"
rating = 9.2
times_viewed = 60
favourite = False
# Python is case-sensitive -> false is not recognised, but False is

# type() function returns the data type of the input
print("The data type of value 'False' is:", type(False))
print("The data type of value '192.' is:", type(192.))

# {data_type}() function casts the input into the specified data type (eg.str(x))
print("\nThe input '\"2\"' when casted into a float is:", float("2"))
print("The input '25.3' when casted into a boolean is:", bool(25.3))
print("The input '3.63' when casted into an integer is:", int(3.63))

# round() function rounds input to decimal places specified (negative d.p. are valid)
print("\nThe input '122.4516' when rounded down to -1 d.p. is:", round(122.4516,-1))
print("The input '122.4516' when rounded down to 0 d.p. is:", round(122.4516))
print("The input '122.4516' when rounded down to 3 d.p. is:", round(122.4516,3))

# len() function returns the size of the input
print("\nThe length of the input 'lesgo G' is:", len('lesgo G'))
# inputting a number will return an error

# strings will follow
print("\n\nStrings follow\n")

# use backslash before single quotes if using both types of quote in a string for correct syntax
quotes_in_string = '"You\'re very talented, he insisted."'
print("\nString with both types of quotes follows:", quotes_in_string)

# plus sign used to concatenate strings
quotes_in_string += ' I was amazed!'
print("\nConcatenated string follows:", quotes_in_string)
print("The new string is of lenght:", len(quotes_in_string))

# multiplication sign used to repeat strings
quotes_in_string *= 4
print("\nRepeating string using '*' follows:", quotes_in_string)

# string methods follow
sample_string = "Dremixis, is an OMNIGOD."
print("\n\nThe sample string used in the following method examples is:", sample_string)

# title() method changes all first letters to uppercase
print("\nThe title() method converts the string to:", sample_string.title())

# islower() method checks whether all characters are lowercase
print("\nThe islower() method returns:", sample_string.islower())

# count() method counts occurrences of a specified string in the sample_string
print("\nThe count('is') method returns:", sample_string.count('is'))

# format() method can replace {} in a string with the specified input
# this method can be really useful in print() statements
print("\n\nThe format() method can modify string output using {}, see code examples")

print("\nThe player named {} always beats G2 in {}v1 situations".format("Faker",3))

counter_champion = "Volibear"
print("\nWhen I pick Darius the enemies counterpick me with {}".format(counter_champion))

# split() method splits string into words separated by a specified separator and returns it as a list of strings
# split(sep, maxsplits) are the possible arguments which are self-explanatory
print("\n\nThe default split() method returns:", sample_string.split())

print("\nWhen the string is separated by ',' we get:", sample_string.split(","))

print("\nWhen the method is split(' ',2) it returns:", sample_string.split(" ",2))

print("\nWhen the method is split(None,7) it returns:", sample_string.split(None,7))

# find() method returns the index of the first occurrence of the specified sample_string
print("\n\nThe first occurence of 'is' in the string starts at index:", sample_string.find("is"))

# rfind() method works in the same way but searches for the last occurrence
print("\nThe last occurrence of 'is' in te string starts at index:", sample_string.rfind("is"))


