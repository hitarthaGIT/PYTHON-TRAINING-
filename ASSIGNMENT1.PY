# 1.Dictionary to Store marks of 5 students where each stuudent has 3 subs
students = {
    "Hitartha": [85, 90, 88],
    "Jane": [78, 82, 80],
    "Devi": [92, 95, 94],
    "Suresh": [60, 65, 70],
    "Lina": [45, 50, 55]
}

# 2.Function to calculate average marks
def cal_avg(marks):
    return sum(marks) / len(marks)

top_scorer = ""
top_average = 0

# 3&4. Assigning grades based on avg marks, and print details
print("Student Results:\n")

for name, marks in students.items():
    avg = cal_avg(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Name: {name}, Average: {avg:.2f}, Grade: {grade}")

    # Finding the top scorer to display later
    if avg > top_average:
        top_average = avg
        top_scorer = name

# 5. Display top scorer
print("\nTop Scorer:")
print(f"Name: {top_scorer}, Average Marks: {top_average:.2f}")
