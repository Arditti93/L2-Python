# time = 19
# place_of_work = "Manchester"
# town_you_live_in = "Sale"

# if time < 8:
#     print(f"The time is before 8am so I am at {town_you_live_in}")
# elif time == 8:
#     print(f"It is 8am so I am communting to {place_of_work}")
# elif time >= 9 and time <= 17:
#     print(f"I am at work in {place_of_work}")
# elif time == 18:
#     print(f"I am going back home to {town_you_live_in}")
# else:
#     print(f"I am at home in {town_you_live_in}")


# username = input("Please enter your username")
# print(f"Hello {username} welcome to my programme")

def add_up(num1, num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def divied (num1, num2):
    return num1 / num2

number_1 = input("Please enter a whole number: ")
number_2 = input("Please enter a second whole number: ")

if number_1.find(".") != -1 or number_2.find(".") != -1:
    print("Sorry please enter a whole number")
else:
    operator = input("Do you want add, subtract or divide your numbers: ")
    number_1 = int(number_1)
    number_2 = int(number_2)

    if operator == "add" or operator == "Add" or operator == "+":
        print(add_up(number_1, number_2))
    elif operator == "/":
        print(divied(number_1, number_2))
    else:
        print(subtract(number_1, number_2))











# The find() method returns -1 if the value is not found. 

# if num_1.find(".") != -1 or num_2.find(".") != -1:
#     print("Please enter a whole number")
# else:
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#     print(f"{num_1} + {num_2} = {num_1 + num_2} ")











