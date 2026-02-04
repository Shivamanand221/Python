class person():
    def __init__(self, n, o):
        self.name=n
        self.occ=o
        print(f"{self.name} is {self.occ}")
        
    def info(self):
        print(f"{self.name} is {self.occ}")

a= person("Ayush", "Dev")
#a.name="Divya"
#a.occ="HR"
#print(a.name)
#a.info()
b= person("Divya", "HR")
a.info()
b.info()
