is_learning = True
is_finished = False
print(f"Are we learning Python? {is_learning}")
print(f"Type of is_learning: {type(is_learning)}")

#Are we learning Python? True
# <class 'bool'>


x = 5
y = 10
print(x < y)   # Is x less than y?
print(x == y)  # Is x equal to y?
print(x != y)  # Is x not equal to y?

# True
# False
# True


name1 = "Alice"
name2 = "Bob"
print(f"Is {name1} before {name2} alphabetically? {name1 < name2}")

# Is Alice before Bob alphabetically? True


a = True
b = False
print(a and b)  # True only if both a AND b are True
print(a or b)   # True if either a OR b (or both) are True
print(not a)    # The opposite of a

# False
# True
# False

#You can also set a variable equal to a Boolean expression:
bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(f"bool_one: {bool_one}, bool_two: {bool_two}, bool_three: {bool_three}")

