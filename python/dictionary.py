# Example of Python dictionary usage

person = {
    "name": "Rohan",
    "age": 28,
    "city": "Mumbai"
}

# Access values
print("Name:", person["name"])
print("Age:", person.get("age"))
print("City:", person.get("city"))

# Add a new key-value pair
person["profession"] = "Data Scientist"
print("Updated person:", person)

person["age"]= 23

# get :  if colour key is not present it will give default value of green.
print(person.get("colour","green")) 

# Iterate over dictionary
for key, value in person.items():
    print(f"{key}: {value}")


# pop

# print(person.pop("profession"))

print(person.popitem())
print(person)

print("age" in person)


# 

# print(person.keys())    keys of dictionary
print(list(person.keys()))

# values 
print(list(person.values()))

#dictionary items

print(list(person.items()))


del person["city"]

personCopy = person.copy()



# Set

s1 = {"Roger", "Sid"}
s2 = {"Roger"}

# intersect = s1 & s2
# print(intersect)

union = s1 | s2 
print(union)

sub = s1-s2
print(sub)

# function



def counter():
    count =0

    def increment():
        nonlocal count
        count+=1

        return count
    
    print(increment())
    print(increment())
    print(increment())


counter()







