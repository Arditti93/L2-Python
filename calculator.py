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