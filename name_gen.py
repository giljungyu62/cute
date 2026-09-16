class Family_name:
    def __init__(self, family_name, main_building, root):
        self.family_name = family_name
        self.main_building = main_building
        self.root = root

class Full_name(Family_name):
    def __init__(self, last_name, family_name, main_building, root):
        super().__init__(family_name, main_building, root)
        self.last_name = last_name
    
    def name_print(self):
        print(self.family_name + self.last_name)

test = Full_name("길준규", "대전", "길자", "존못")
print(test.name_print())