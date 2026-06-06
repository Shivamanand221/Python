class Person:
    name = "abc"
    occ = "eng"
    gender = "boy"

    def info(self):
        print(f"{self.name} is a {self.occ}")
    def info2(self):
        print(f"{self.name} is a {self.gender}")

a = Person()
a.name = "Ayush"
a.occ = "eng"
a.gender = "boy"
print(a.name)
a.info()
a.info2()
