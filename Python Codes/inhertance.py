class Animal:
    def breathe(self):
        print("breathing")
class Fish(Animal):
    def breathe(self):
        Animal.breathe(self)
        print("underwater")
nemo = Fish()
nemo.breathe()
#Result:
#breathing
#underwater