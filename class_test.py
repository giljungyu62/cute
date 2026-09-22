class First:
    def __init__(self):
        self.name = "첫번째"

class Second:
    def __init__(self):
        self.name = "두번째"


class First_age(First):
    def __init__(self):
        super().__init__()
        self.age = 27

age_test = First_age()
print(age_test)
