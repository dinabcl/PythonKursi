from abc import ABC

class Person(ABC):
    def __init__(self, name, age, weight,height):
        self.name=name
        self.age= age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,weight):
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


    def calculate_bmi(self):
        pass

    def get_bmi_category(self,adult_bmi):
        pass

    def print_info(self):
        pass


class Adult(Person):
    def __init__(self, name, age, weight,height,adult_bmi):
        super().__init__(name, age, weight,height)
        self.adult_bmi = adult_bmi


    def calculate_bmi(self):
        adult_bmi = self._weight/self._height
        return adult_bmi

    def get_bmi_category(self,adult_bmi,):
        if adult_bmi < 18.5:
            return "Underweight"
        elif 18.5 < adult_bmi < 24.9:
            return "Normal"
        elif 24.9 <  adult_bmi < 29.9:
            return "Overweight"
        elif adult_bmi >= 29.9:
            return "Obese"
        else:
            return "Try again"


class Child(Person):
    def __init__(self, name, age, weight, height, child_bmi):
        super().__init__(name, age, weight, height)
        self.child_bmi = child_bmi

    def calculate_bmi(self):
        child_bmi = self._weight / self._height * 1.3
        return child_bmi

    def get_bmi_category(self, child_bmi):
        if child_bmi < 14:
            return "Underweight"
        elif 14 < child_bmi < 18:
            return "Normal"
        elif 18 < child_bmi < 24:
            return "Overweight"
        elif child_bmi >= 24:
            return "Obese"
        else:
            return "Try again"


class BmiApp(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name,age,weight,height)
        self.people = []


    def add_person(self,person):
        self.people.append(person)

    def collect_user_details(self):
        self.name = input("Whats your name?")
        self.age = int(input("Whats your age?"))
        self.weight = float(input("Whats your weight?"))
        self.height = float(input("Whats your height?"))
        if self.age.add_person(self) <18:
            return Child.calculate_bmi()
        else:
            return Adult.calculate_bmi()

    def print_result(self):
        pass

print(BmiApp.collect_user_details())