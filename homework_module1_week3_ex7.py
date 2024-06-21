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

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Name: {self._name}, Year of Birth: {self._yob}, Specialist: {self._specialist}")

# Testing the implementation
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist ="Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()