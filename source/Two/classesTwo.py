# OOP = object oriented programming
class Person:
    '''This is the parent class'''
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        error = f"{self.name}, {self.age}, {self.course}"
        return error

    def changeName(self, new_name):
        '''this function changes the name of the studen'''
        self.name = new_name

    def changeAge(self, new_age):
        '''Change the age of the user'''
        self.age = new_age

    def changeCourse(self, new_course):
        '''Change the age of the user'''
        self.age = new_age


class Teachers(Person):
    '''This class inherits from the person class'''
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def canFailStudent(self):
        return True

# # # __init__ method
class Student(Person):
    '''This class inherits from the person class'''
    def __init__(self, name, age, course, average):
        self.name = name
        self.age = age
        self.course = course
        self.average = average

    def changeAverage(self, new_ave):
        '''This function changes the average of the student'''
        self.average = new_ave

    def canTrailCourse(self):
        return True


# # # using the super method
class NonTeachingStaff(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age, course)

TA = NonTeachingStaff("Abdul Haqq", 56, "Electrical")

print(TA.name)
print(TA.age)
print(TA.course)
print(TA.__repr__())


student1 = Student("Abdul Haqq", 56, "Electrical", 98)
# print(student1.name)
# student1.changeName("Yakubu")
# print(student1.name)
# print(student1.average)
# student1.changeAverage(99)
# print(student1.average)

# print(type(student1))

# print(student1.name)
# print(student1.age)
# print(student1.course)
# print(student1.average)

# print(student1.name)
# student1.changeName("Yakubu")
# print(student1.name)
# print(student1.average)
# student1.changeAverage(99)

teacher1 = Teachers("Dr.Opoku", 56, "custom")

# print(teacher1.name)
# print(teacher1.canFailStudent())