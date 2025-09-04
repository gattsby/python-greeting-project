name = "Jake Newberry"  # String
age = 26  # Integer
hobby = "gaming and hanging out with my cat, Roo"  # String

print(name)
# Testing to make sure it prints my name correctly first.
print("Hi, my name is " + name + ".")
# Prints my name in a sentence.
print("Hi, my name is " + name + ", and I am " + str(age) + ".")
# My first instinct was to try and and use the integer data type, but since Python assumes you don't want to add a string and an integer together, I had to convert the integer to a string using the str() function.
print("Hi, my name is " + name + ", I am " +
      str(age) + ", and I love " + hobby + ".")
# Prints my name, age, and hobby in a sentence.https://github.com/gattsby/python-greeting-project.git
