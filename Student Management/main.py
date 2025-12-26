# Different import styles (Q5)
import student
from marks import cal_avg, cal_grade
import attendance as att
import fees
from reports import Report
import utils
import random
import math

# Student Data
student.add_student(101, "Hitartha Saikia")

marks = [80, 85, 90]

if utils.validate_marks(marks):
    avg = cal_avg(marks)
    grade = cal_grade(avg)

attendance_percent = att.attendance_percentage(48, 50)
fee = fees.fee_status(30000, 30000)

# Random roll demo
roll = random.randint(100, 999)

# Math module demo
rounded_avg = math.ceil(avg)

# Report
r = Report("Rahul", rounded_avg, grade, attendance_percent, fee)
r.generate()

# Module properties (Q9)
print("\nModule Info:")
print(student.__name__)
print(student.__file__)
print(student.__dict__)
