from enum import Enum

name = "Rohan"
age = 15

# invalid variable names are those which start with number and it has special 
# characters like %, $ .  _ is valid.
# your variable name cannot be a keyword

print(type(age))
print(type(name))

age1 = 12.2

print(type(age1))

# we can convert a integer to float using class constructor like

dec = float(age)

print(type(dec))

# we can compare whethte the instance of age is int or not using isinstance()

print(isinstance(age, int))
print(isinstance(age, str))

# ternary operator


def age_check():
    return True if age > 12 else False


print(age_check())

print(name.upper())
print("WskY".lower())

print("roHan sharMa".title())
print("rohan".islower())

print(len(name))


print ("ha" in name)

print(name + "\'"+"s")

# any keyword is for boolean values and it returns true if any of the thing
# is true

val_1 = True
val_2 = False

result_bool = any([val_1 , val_2 ])

print(result_bool)


# Imaginary numbers 

num1 = 2 + 3j

print(num1)

num2 = complex(5,1)

print ( num2.real, num2.imag)
print(num2)

# built in functions for numbers

print(abs(-4.3))  # convert the negative value into positive

print( round(7.59))  # round the 7.59 to 8 

print(round(7.59,1)) # round 7.59 to 10th place 

# Enum

class State(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(State)
print(State.ACTIVE)
print(State.ACTIVE.value)
print(list(State))
print(len(State))

# output of above print statement 
# <enum 'State'>
# State.ACTIVE
# 1
# [<State.ACTIVE: 1>, <State.INACTIVE: 0>]
# 2