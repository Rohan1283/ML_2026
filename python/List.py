
List = ["Rohan", 1, True, "bool",45]

print(True in List)

List.append("Swayam")  # Allows only single element to add at a time

print(len(List))
print(List)

List.extend(["hello","rohit"])   # for multiple element addition we use extend
print(List)

# += works the same as extend for example

List += ["numo", "namah"]

print(List)

List.remove("hello")

print(List)

print(List.pop())
print(List)

List.insert(2, "sharma")
print(List)

List[1:1] = ["believe","sharma"]
print(List)


List2 = ["Rohan", "rohan", "hi","Hello", "what","Koi baat nahi"]

List2.sort()
List2.sort(key = str.lower)

# The first statement, list2.sort(), puts all capital letters before lowercase 
# letters. The second statement, list2.sort(key = str.lower), ignores capital 
# letters completely and sorts the words in true alphabetical order.

print(List2)
print(sorted(List2,key=str.lower))

# Tuples

tuple1 = ("sharmaaa", "jiii")

print(tuple1[0])
print(tuple1.index("jiii"))

print(len(tuple1))

print(sorted(tuple1,key=str.lower))