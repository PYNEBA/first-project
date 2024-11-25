# int  price = 10
# float rating = 4.9
# string name= ("Mosh")
# boolean is_published = False
#from itertools import count_n
#from operator import countOf

# INPUT FROM THE USER
#name = input("enter your name : ")
#print ("hi "+name)

#birth_year = int(input("Enter your birth year: "))
#age = 2024 - birth_year
#print( age)


#Converting pounds to kilograms
#weight_pl = input("Enter your weight in pounds: ")
#weight_kg = int(weight_pl)*1.65
#print(weight_kg)

#course = "Python's course for beginners "
#course = 'python for "Beginners"'
#print(course)

#course = "Python for Beginners"
#print(course[0:3])
#print(course[-2])

#name = "jennifer"
#print(name[1:-1])

#first = 'John'
#message = first + ' ['+ last+'] is a coder'
#msg = f'{first} [{last}] is a coder '
#print(msg)

#course = 'Python for Beginners'
#print(len(course))
#print(course.upper())
#print(course.lower())
#print(course.find('o'))
#print(course.replace('Beginners','absolute Beginners'))
#print(course.replace('P', 'J'))
#print('Python' in course)
#print('python' in course)

 #print(10+3) # for addition
#print(10-3) # for subtraction
#print(10/3) # for division with whole decimal number
#print(10//3) # for division only whole number result
#print(10%3) # for reminder
#print(10**2) # for power or exponent

#x=10
#x=x+3
#x+=10
#print(x)

#x=3.9
#print(round(x))
#print(abs(-1.1))

#import math
#print(math.floor(2.1))
# python 3 math module# Password Validator without 'is_valid' flag
# print("Welcome to the Password Validator")
#
# password = input("Please enter your password: ").strip()
# reasons = []  # Only use 'reasons' list to track invalid conditions
#
# # Check 1: Length of at least 8 characters
# if len(password) < 8:
#     reasons.append("Password must be at least 8 characters long.")
#
# # Check 2: Contains at least one uppercase letter
# if not any(char.isupper() for char in password):
#     reasons.append("Password must contain at least one uppercase letter.")
#
# # Check 3: Contains at least one lowercase letter
# if not any(char.islower() for char in password):
#     reasons.append("Password must contain at least one lowercase letter.")
#
# # Check 4: Contains at least one digit
# if not any(char.isdigit() for char in password):
#     reasons.append("Password must contain at least one number.")
#
# # Check 5: Does not contain spaces
# if " " in password:
#     reasons.append("Password must not contain any spaces.")
#
# # Determine validity based on 'reasons' list
# if not reasons:
#     print("Your password is valid!")
# else:
#     print("Your password is invalid for the following reasons:")
#     for reason in reasons:
#         print(f"- {reason}")

#is_hot = False
#is_cold = False

#if is_hot :
   # print("it's a hot day")
   # print("drink pleanty of water")
   # print("Enjoy your day")
#elif is_cold :
   # print("be aware of coldness")

#else:
    #print("it's lovely day")

# and Operator
#has_high_income= True
#has_good_credit= True
#if has_high_income and has_good_credit :
 #   print("Eligible for the loan")

# OR operator
#has_high_income= False
#has_good_credit= True
#if has_high_income or has_good_credit :
   # print("Eligible for the loan")


## PROJECT NEW 1
#is_hot = False
#if is_hot:
 #print("It's a hot day")
# print("Drint plenty of water")
#else:
 #print("It's a cold day")
# print("Wear warm clothes")
# print("Enjoy your day")



## PROJECT 3

#is_hot = False
#is_cold = True

#if is_hot:
   #print("It's a hot day")
   #print("Drink plenty of water")
#elif is_cold:
   #print("It's a cold day")
   #print("Wear warm clothes ")
#else:
   #print("It's a lovely day")

#print("Enjoy your day")

## PROJECT NEW 3

#price = 1000000
#has_good_credit = True

#if has_good_credit:
    #down_payment = 0.1 * price
#else:
     #down_payment = 0.2 * price

#print(f"Down payment : ${down_payment}")




## PROJECT NEW 4


#temperature = 30
#if temperature >30:
   #print("It's a hot day ")
#elif temperature <10:
   # print("It's a cold day")
#else:
   # print("It's a neither a hot nor cold day")


##PROJECT NEW 5

#name = input("Enter your name: ")
#if len(name)<3:
   # print("name must be at least 3 characters")
#elif len(name)>50 :
    #print("name can be a maximum of 50 characters ")
#else:
   # print("name looks good")

## PROJECT NRE 6

#weight = int(input("weight: "))
#character = input("(L)lbs or (K)g: ")

#if character.upper()=="L":
 #   converted = weight * 0.45
  #  print(f"you are {converted} pounds")
#else:
 #   converted = weight //0.45
  #  print(f"you are {converted} kilos ")

## PROJECT NEW 7 = WHILE LOOP

#i = 1
#while i<=5:
   # print(i)
   #i = i+1
#print("Done")

## Guess game(P7)

#secret_number = 8
#guesses_made = 0
#limit_given = 4
#uesses_made+=1

#while guesses_made < limit_given:
    #guesses_made += 1
    #guess = int(input("Guess: "))

   # if guess == secret_number:
      #  print("Congrats, you won")
      #  break
    #else:
       # print("Try again")

#else:
      #  print("you have completed your all 3 chances ")





## (P8) CAR GAME



#while True:
   # command = input(">").lower()

   # if command == "start":
    #    print("Car started...")
    #elif command == "stop":
    #    print("Car stopped.")
  #  elif command == "help":
      #  print("""
   # start - To start the car
   # stop - To stop the car
  #  quit - To quit      """)

  #  elif command == "quit":
    #    break
  #  else:
   #     print("Sorry, I don't understand that")

## (P9)

## P8

#while True:
     #command = input("> ").lower()

    # if command =="start":
      #   if  started:
        #     print("Car is already started!")
        # else:
         #    started = True
          #   print("Car started...")
  #   elif command == "stop":

      #   if not started:
          #   print("Car is already stopped!")
       #  else:
          #   started = False
          #   print("Car stopped.")

    # elif command =="help":
       #  print("""
        # start - To start the car
       #  stop - To stop the car
       #  quit - To exit """)

   #  elif command == "quit":
       #  break

    # else:
        # print("Sorry, I don't understand that!")



## P9  / for loop
#prices = [10, 20 , 30]
#total = 0

#for price in prices:
 #total +=price
#print(f"total is :{total}")

# P10/ nested loop

#numbers  = [5,2,5,2,2]
#for x_count in numbers:
 #    output = ''
  #   for count  in range (x_count):
   #       output +='x'
    #print(output)


#excercise  for lists

#names[0] = 'Jhon'
#print(names[0])
#print(names[2:])


#Project 11/ lists

#numbers =[1,3,4,5,6,11,23,34,45]
#max = numbers[0]
#for number in numbers:
   # if number > max:
       #   max = number

#print(max)



##  PROJECT 12/ 2D lists

#matrix = [
 #   [1,2,3],
  #  [4,5,6],
   # [7,8,9]
#]
#   for item in row:
 #       print(item)

## List method

#numbers = [5,2,1,7,4]
#numbers.insert(3,3)
#print(numbers)

## Write a program to remove the duplicate in a list.

#numbers = [2,2,4,6,3,4,6,11]
#uniques = []
#for numbers in numbers:
   #if numbers not in uniques:
       # uniques.append(numbers)

#print(uniques)

## Tuples

#numbers = (1,2,3)
#numbers[0] = 10
#print(numbers[0])

## unpacking

#coordinate = [1,2,3]
#x,y,z = coordinate
#print(x)

## Dictionaries

#customer = {
 #   "name" : "John smith",
  #  "age": "30",
   # "is_verified": "True"

#}
#customer["name"]= "baburam"
#print(customer.get("Birth_year","name"))

## Convert the numbers into word

#phone = input ("phone: ")
#digital_mapping = {
 #   "1": "one",
  #  "2": "Two",
   # "3": "Three",
 #"4": "Four"

#}
#output = ""
#for ch in phone:
 #  output += digital_mapping.get(ch, "!") + " "
#print(output)

## Eomojis converter with dictionaries
#message  = input(">:")
#words = message.split(" ")
#emojis = {
#   ":)" : "😊",
#    ":(" : "🙁"

#}
#output = ""
#for word in words:
#   output +=emojis.get(word, word) + " "
#print(output)




## Functions

#def user_family():
   # print("Baburam")
  #  print("Ghan b. kc")


#print("Welcome all of you")
#user_family()


## Parameters

#def greet_user(first_name, last_name):
    #print(f"Hi {first_name} {last_name}")


#print("Star")
#greet_user("Baburam", "Kc")
#print("Welcome to abroad")



#Keywords arguments

#def greet_user(first_name, last_name):
    #print(f"Hi {first_name} {last_name}")



#print("Star")
#greet_user("Baburam", "Kc") # positional arguments, [first name = baburam, last name = kc]
#greet_user("kc", last_name = "Manisha") # keywords arguments, [automatic by function or postional arguments first name = kc, by keywords arguments last name = manisha]
#print("Welcome to abroad")


## Return statement #(return statement is used to return the value to fucntiosn like here square)
#def square(number):
  # return  number * number


#print(square(3))


## Emojis converter with functions

#def emojis_converter(message):
#    words = message.split(" ")
#    emojis = {
#        ":)": "😊",
#        ":(": "🙁"
#
#   }
#    output = ""
#    for word in words:
#       output += emojis.get(word, word) + " "
#
#   return output
#
#
#message = input(">")
#print(emojis_converter(message))

## Error handling

#try:
#    age = int(input("Age:"))
#   income = 20000
#    risk = income / age
#    prnt(age)

#except ZeroDivisionError:
#    print("Age cannot be 0.")

#except ValueError:
#    print('Invalid value:')


## Classes
















































