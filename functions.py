def press_grind_beans():
    print("Coffee Machine is grinding the beans")


press_grind_beans()

x = input("Please enter an amount")
y = input("Enter your account number")

def cash_machine(amount, accum):
    print(f"withdrawing {amount} from account {accum}")


cash_machine(x, y) 
cash_machine(300, 123456)
# this runs the function and any code inside it will run


drink_size = "Small"
drink_type  = "Flat White"

def take_order(size, type_of_drink):
    print(f"I'd like a {size} {type_of_drink} please")

take_order(drink_size, drink_type)
take_order("large", "Latte")
take_order("Medium", "Hot Chocolate")

num1 = int(input("enter a number "))
num2 = int(input("enter a second number "))

number_1 = 20
number_2 = 40

def add_up(num1, num2):
    return num1 + num2

print(add_up(number_1, number_2))
print(add_up(4, 5))
print(add_up(200, 560))






