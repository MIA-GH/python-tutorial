# # # tuple is immutable = cannot be modified
# list is mutable = can be modified

myTuple = ("Name", "Age", "Course")
# print(myTuple)
# This gives an error
# myTuple + ("Nana")
newTuple = ("Abdul", 54, 56.9, True)
# print(newTuple)

# print(type(myTuple))

nTp = tuple(("Name", "Age", "Course"))
# print(nTp)
# print(myTuple[-2])
# print(myTuple[1])

fruits = ("apple", "banana", "mango", "oranges", "melon", "berry", "kiwi")
# print(fruits[2:5])
# print(fruits[2:])
# print(fruits[2:-1])
# print(fruits[:4])
# print(fruits[0:4])

# if "cherry" in fruits:
#     print("Yes")
# else:
#     print("No")

# print("apple" in fruits)

# new_fruits = list(fruits)
# print(new_fruits)
# new_fruits[4] = "New Item"
# # print(new_fruits)
# new_tuple = tuple(new_fruits)
# print(new_tuple)

# unpacking tuples
# print(len(fruits))
nl  = fruits[2:5]
# print(nl)
(one, two, three) = nl
# print(one)
# print(two)
# print(three)

# (fav, se_fav, th_fav, *rem,) = fruits
# (fav, se_fav, *rem, th_fav,) = fruits
# (*rem, fav, se_fav,  th_fav,) = fruits
# print(fruits)
# print(fav)
# print(se_fav)
# print(th_fav)
# print(rem)

# # # looping through tupples
# for item in fruits:
#     print(item)

# for i in range(len(fruits)):
#     print(fruits[i])

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

newTp = fruits + myTuple
# print(newTp)
# print(myTuple * 2)
# npl = list(myTuple)
# print(npl * 2)

# tuple methods
# count()
# index()

mytpl = ("Musah", "Rahman", "Musah", "Rahman")

print(mytpl.index("Rahman"))
print(mytpl.count("Rahman"))