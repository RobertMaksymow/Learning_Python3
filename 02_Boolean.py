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


is_raining = True

if is_raining:
  print("bring an umbrella")

if 2 == 4 - 2: 
  print("apple")


# Relational operators are used to compare values. The result of a comparison is a Boolean value: True or False.
x = 20
y = 20

if( x == y):
  print("These numbers are the same."
)

# AND
statement_one = 2 + 2 + 2 >= 6 and -1 * -1 < 0
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)


credits = 120
gpa = 3.4

if (credits >= 120 and gpa >= 2.0):
  print("You meet the requirements to graduate!")

# OR

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if(credits >= 120 or gpa >= 2.0):
  print("You have met at least one of the requirements."
)

#NOT
statement_one = not (4 + 5 <= 9)
print(statement_one) #False

statement_two = not (8 * 2) != 20 - 4
print(statement_two) #True



credits = 110
gpa = 1.8

if(not credits >= 120):
  print("You do not have enough credits to graduate."
)

if(not gpa >= 2.0):
  print("Your GPA is not high enough to graduate."
)

if(not credits >=120 and not gpa >= 2.0):
  print("You do not meet either requirement to graduate!")