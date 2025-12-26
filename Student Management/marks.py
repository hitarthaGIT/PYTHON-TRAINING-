def cal_avg(marks):
    return sum(marks) / len(marks)

def cal_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"
