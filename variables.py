# --------------------------------------------
# DATA TYPES
# --------------------------------------------

# print("hello world") 
# String data type represents text

# print(5)
# Interger represents a whole number

# print("6")
# this is not a interger its a string 

# print(3.15)
# this a a floating point it represents a decimal number

# print(True)
# this is a boolean, it represents either true or false
# they must start with a capital letter
# print(False)

# --------------------------------------------
# VARIABLES
# --------------------------------------------

my_name = "Alex"
# print(my_name)
age = 30 
# print(age)
student = False
# print(student)
student = True
# assiging the student variable new data, not creating a new variable
# print(student)
student = "I am not a Student"
# print(student)
sentance = "My name is "
print("My name is " + my_name)


fav_drink = "Pepsi"
print(f"Hello my name is {my_name} and my fav drink is {fav_drink}")

print(len("hello"))
print("hello"[1]) 
# the letter e prints in the terminal as python starts counting at 0 not 1

text = "hello world"
print(text.upper())

lower_case = "hello WORLD"
print(lower_case.lower())

cap = "hello everyone"
print(cap.capitalize())

text2 = "hello, hello is this thing on"
print(text2.count("hello"))

text3 = "hello"
print(text3.count("l"))

txt = "Hello, welcome to my world." 
print(txt.find("welcome"))

text4 = "I like pasta"
print(text4)
print(text4.replace("pasta", "curry"))

text5 = "       rice       "
print(text5)
stripped_txt = text5.strip()
print(f"my fav food is {stripped_txt}")












