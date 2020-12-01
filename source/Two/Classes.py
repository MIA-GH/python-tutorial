# OOP = object oriented programming
class Teachers:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def changeAge(self, new_age):
        '''Change the age of the user'''
        self.age = new_age

# name, age, course, average
class Student:
    def __init__(self, name, age, course, average):
        self.name = name
        self.age = age
        self.course = course
        self.average = average

    def changeName(self, new_name):
        '''this function changes the name of the studen'''
        self.name = new_name

    def changeAverage(self, new_ave):
        '''This function changes the average of the student'''
        self.average = new_ave


student1 = Student("Abdul Haqq", 56, "Electrical", 98)
print(student1.name)
student1.changeName("Yakubu")
print(student1.name)
print(student1.average)
student1.changeAverage(99)
print(student1.average)

# print(student1.age)
# print(student1.course)
# print(student1.average)
# print(type(student1))