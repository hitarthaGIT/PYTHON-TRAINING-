def validate_marks(marks):
    return all(0 <= m <= 100 for m in marks)
