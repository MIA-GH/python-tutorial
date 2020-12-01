import random
# # # conditionals
# if, else, elif (else if)

age = 49   

# if age > 18:
#     print("You can enter")
# else:
#     print("You are under age")



# if age < 18:
#     print("You are under age")
# elif age > 18 and age < 50:
#     print("Gate free for you")
# else:
#     print("You can enter")


number = random.randint(0,10)
print(number) # show the generated number
if number == 0:
    print("The nuber is ", number)
elif number > 1 and number < 5:
    print("heads")
else:
    print("tails")