# To create a student utility module

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def find_grade(percentage):

    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"