# Lists can contain more than just numbers.

empty_list = []
ints_and_strings = [1, 2, 3, "four", "five", "myname"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]




# APPEND ITEMS
orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# Prints ['cake', 'cookie', 'bread', 'biscuit', 'tart']


my_list = [1, 2, 3]
my_new_list = my_list + [4, "text"]
print(my_new_list)
# Prints [1, 2, 3, 4, "text"]

# ACCESS ITEMS
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)


# Negative Index
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element)
print(index5_element)
# Print 'cereal'


# Modifying
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
garden[-1] = "Raspberries"

print(garden)


# REMOVE ITEMS
# If we use .remove() on a list that has duplicate elements, 
# only the first element that matches the specified value is removed:
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

shopping_line.remove("Chris")
print(shopping_line)
# ["Cole", "Kip", "Sylvana", "Chris"]

order_list = ["Celery", 'Orange Juice', 'Orange', 'Flatbread']
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)

# new_store_order_list.remove("Onions") - ValueError: list.remove(x): x not in list

# Two-Dimensional (2D) Lists
heights = [["Noelle", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
#Access the sublist at index 0, and then access the first index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

mixed_list = [1, "hello", 3.14, [1, 2, 3]]
print(mixed_list)
print(mixed_list[3][1])
print(mixed_list[-1][-1])
# Print 2 and 3

class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
print(class_name_hobbies)
# The list of Jenny is at index `0`. The hobby is at index `1`. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
# The list of Grace is the last entry. The hobby is the last element. 
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)

