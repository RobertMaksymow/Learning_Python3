weekday = True
if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")

age = 12
if age >= 13:
  print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")

credits = 120
gpa = 1.9
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

# If-Else statement
user_name = "Dave"  
if user_name == "Dave":   
    print("Get off my computer, Dave!")   
elif user_name == "angela_catlady_87":   
    print("I know it is you, Dave! Go away!")   
elif user_name == "Codecademy":   
    print("Access Granted.")   
else:   
    print("Username not recognized.")  

# Switch statement
user_name = "Dave" 
match user_name:
    case "Dave":
        print("Get off my computer, Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:
        print("Username not recognized.")  