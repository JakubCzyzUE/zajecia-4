

def main():
    s1 = Student("Karol Kozłowski",60)
    s2 = Student("Jacek Jackowski",30)

    s1.is_passed()
    s2.is_passed()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def is_passed(self):
        print(self.name)
        if(self.marks > 50):
            print("ocena" + self.name + "studenta jest większa niż 50")
            return True
        elif(self.marks < 50):
            print("ocena" + self.name + "studenta jest mniejsza niż 50")
            return False
