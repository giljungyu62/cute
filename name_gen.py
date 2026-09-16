class Family_name:
    def __init__(self, name):
        self.name = name

class Last_name:
    def __init__(self, name):
        self.name = name

a = Family_name("길")
b = Last_name("준규")

full_name = a.name + b.name
print(full_name)