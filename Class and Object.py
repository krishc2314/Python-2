class Student:
    def __init__(self):
        self.name = " "
        self.roll_no = 0
        self.marks = {}
        self.sum = 0
        self.avg =0

    def acceptdetails(self):
        self.name = input("Enter your name: ")
        self.roll_no = int(input("Enter your roll number: "))
        
        n = int(input("Enter the number of subjects you have: "))

        for i in range(n):
            subject = input("Enter the subject's name: ")
            mark = int(input(f"Enter the marks for {subject}: "))
            self.marks[subject] = mark
            self.sum += mark
        
        self.avg = self.sum/n
    
    def total(self):
        print(f"Total marks: {self.sum}")
    
    def average(self):
        print(f"Average marks: {self.avg}")

    def display_details(self):
        print(f"Student Name: {self.name}\nRoll Number: {self.roll_no}\nYour marks are:")
        for subject in self.marks:
            print(f"{subject} : {self.marks[subject]}")
        self.total()
        self.average()

student1 = Student()
student1.acceptdetails()
student1.display_details()


        