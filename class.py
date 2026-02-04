class Person:
    name = "abc"
    occ = "eng"
    gender = "boy"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person()
a.name = "Ayush"
a.occ = "eng"
a.gender = "boy"

print(a.name)
a.info()

