class Student:
    def __init__(self,name, age, height, everageMark):
        self.name = name
        self.age = age
        self.height = height
        self.everageMark = everageMark

Mila = Student(name="Mila", age=13, height=167, everageMark=12)
print(Mila.name, Mila.age, Mila.height, Mila.everageMark)

Kyrylo = Student(name="Kyrylo", age=12, height=152, everageMark=12)
print(Kyrylo.name, Kyrylo.age, Kyrylo.height, Kyrylo.everageMark)

Alexander_1 = Student(name="Alexander", age=14, height=174, everageMark=12)
print(Alexander_1.name, Alexander_1.age, Alexander_1.height, Alexander_1.everageMark)

Alexander_2 = Student(name="Alexander", age=14, height=180, everageMark=12)
print(Alexander_2.name, Alexander_2.age, Alexander_2.height, Alexander_2.everageMark)