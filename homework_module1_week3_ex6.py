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

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Name: {self._name}, Year of Birth: {self._yob}, Subject: {self._subject}")

# Testing the implementation
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 2011
teacher1.describe()