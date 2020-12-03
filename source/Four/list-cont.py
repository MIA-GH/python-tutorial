# list

# myList = [2,4,6,5,7,8]

# for i in myList:
#     print(i)
# newList = [expression for item iterable if condition else some statement]
newList = ["Musah", "Rahman", "Sufyan", "Haqq", "Rafiu", "Book", "Going"]
# traditional program
# li = []
# for item in newList:
#     if "a" in item:
#         li.append(item)
# print(li)
# ll = []
# myList = [ll.append(x) for x in newList if "a" in x]
myList = [x for x in newList if "a" in x]
# print(myList)

number = [1,2,3,4,5,6,7,8,9]
selectedNumber = [num for num in number if num > 5]
# print(selectedNumber)
generatedList = myList + selectedNumber
print(generatedList)

nl = myList.copy()
# print(nl)
nl.extend(selectedNumber)
print(nl)