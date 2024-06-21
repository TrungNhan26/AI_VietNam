from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    #lớp trừu tượng được khai báo nhưng không được định nghĩa cụ thể,chỉ được định nghĩa cho lớp con
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Name: {self._name}, Year of Birth: {self._yob}, Grade: {self._grade}")

# Testing the implementation
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()