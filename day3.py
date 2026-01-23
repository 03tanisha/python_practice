class Student:
    def __init__(self, name):
        self.name = name

class Course(Student):
        def __init__(self, name,cr_name):
            super().__init__(name)
            self.cr_name = cr_name

c = Course("tanisha","ai")
print(c.name)
print(c.cr_name)


class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def barks(self):
        print("dog barks")

d = Dog()
d.sound()
d.barks()


class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

if __name__ == "__main__":
    s = Student("tanisha",4)
    print(s.name)
    print(s.roll_no)


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)
        self.department = department

if __name__ == "__main__":
    m = Manager("tanisha",50000, "mle")
    print(m.name)
    print(m.salary)
    print(m.department)




