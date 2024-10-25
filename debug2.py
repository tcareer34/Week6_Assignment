def score_to_letter_grade(grade):

    if grade >= 90:
        return "A"
    elif grade >= 87:
        return "B+"
    elif grade >= 80:
        return "B"
    elif grade >= 77:
        return "C+"
    elif grade >= 70:
        return "C"
    elif grade >= 67:
        return "D+"
    elif grade >= 60:
        return "D"
    else:
        return "F"


user_score = float(input('Enter your grade'))
print(f'your grade in letter is:', (score_to_letter_grade(user_score)))
