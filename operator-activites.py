from datetime import datetime

# 1 
# Arithmetic Operators
num_1 = 6
num_2 = 4
# +
print(num_1 + num_2)

# -
print(num_1 - num_2)

# / 
print(num_1 / num_2) 

# %
print(num_1 % num_2) 

# **
print(num_1 ** num_2)

# //
print(num_1 // num_2)

# Assigment Operators
x = 5 
print(x)

x += 3 
# x = x + 3
print(x)

x -= 3
# x = x - 3
print(x)

x *= 3
# x = x * 3
print(x)

x /= 3
# x = x / 3
print(x)


# 2
today = datetime(2024,7,8)
bday = datetime(2024,10,1)

difference = bday - today 
print(difference)
print(str(difference) + " days until your birthday")





