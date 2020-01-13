# Python 101

# Declare a var
sum = 2 + 2
# print(sum)
# Comparisons use double equal
# print(sum == 4)

# Varuables adhere to scope, kind of like let in JS...
name = "Fred"
def say_name():
    # ...unless you use 'global'
    # global name
    name = "Bubba"
    print("internal", name)

# say_name()
# print("external", name)


# if/else
name = "Joe"
if name == "Steve":
    print("I feel great")
elif name == "Joe":
    print("You got the better instructor")
else:
    print("I have a cold")

# string concatenation
# print(f"My name is {name}")
# Still have dynamic typing ( but no implicit coercion!)
# Can't do this:
# print(2 + "2")

#****Collections*******
# List
junk = ["Fred", True, [1,2,3], 234]

junk.append("uh-oh")
junk.insert(3, "oh, I get it")
junk.extend(["Mary", "Joseph", "Bob"])
print(junk)

#You can declare an empty list:
stuff = []


# Dictionaries
my_pairs = {
  123: "number",
  "name": "Broomhilda"
}

print(my_pairs["name"])

# Add new properties
my_pairs["last"] = "Jones"
my_pairs["address"] = {"number": 123, "street": "Sesame St" }

# Access different parts of the dict
print(my_pairs.keys())
print(my_pairs.values())
print(my_pairs.items()) # outputs a list of tuples!

# Access nested data
street_name = my_pairs["address"]["street"]
print(street_name)

# You can declare an empty dict
my_dict = {}

# Sets
my_stuff = {"Fred", True, 123, "Jones", "Fred"}
# print(my_stuff) # No duplicates allowed! Bye, extra Fred

# Turn a set into a list, if you want to
print(list(my_stuff))
print(my_stuff)

# Turn a list into a set, then back into a list. Trick for removing duplicate values from your list
list_of_names = ["Mary", "Joseph", "Bob", "Joseph"]
unique_list = list(set(list_of_names))
print('no dupes!', unique_list)

# Put more stuff into a set
my_stuff.add("Feed me")
print(my_stuff)

# You cannot declare an empty set this way. Python thinks it's a dict
my_hmmmm = {}
# but you can do this
my_hmmmm = set()
print("set?", my_hmmmm)
my_hmmmm.add("lonely string")
print("set?", my_hmmmm)


# tuple: Are immutable. Can't add or remove anything from them
my_tup = (1, 2, 3, 3, "hello")
# print(my_tup)

# Nope
# print(my_tup[0])

# You CAN reassign a variable to a new tuple, though.
my_tup = ("WTF", "I'm hungry")
print(my_tup)

# If you have one value in a tuple, you have to follow it with a comma
my_little_tup = ("hello",)
print(isinstance(my_little_tup, tuple))

#joins
names = ["Mary", "Joseph", "Bob"]
# print(", ".join(names))

# loops: for...in works for any of these collectionse
my_tup = (1, 2, 3, 3, "hello")
my_set = {1, 2, 3}
junk = ["Fred", True, [1,2,3], 234]
for foo in junk:
    print(f"Why do I still have {foo} in this drawer?")


my_dict = {
    123: "number",
    "name": "Broomhilda"
}
for foo in my_dict.keys():
    print(f"Why do I still have {foo} in this drawer?")


# create a new list from a subset of values in another list with slice
my_list = [1, 2, 4, "hello", "monkey"]
my_subset = my_list[0:3]
my_subset = my_list[1:3]
my_subset = my_list[:3]
my_subset = my_list[2:]
my_subset = my_list[2:34]
my_subset = my_list[2:-1]
print(my_subset)
print(my_list)
