import datetime

class Report:
    def __init__(self, name, avg, grade, attendance, fee):
        self.name = name
        self.avg = avg
        self.grade = grade
        self.attendance = attendance
        self.fee = fee
        self.date = datetime.date.today()

    def generate(self):
        print("\n***** Student Repot *****")
        print("Name:", self.name)
        print("Average:", self.avg)
        print("Grade:", self.grade)
        print("Attendance:", self.attendance, "%")
        print("Fee Status:", self.fee)
        print("Date:", self.date)
