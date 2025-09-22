def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Input
name = input("Enter the student name: ")


g1 = float(input("Enter grade 1: "))
g2 = float(input("Enter grade 2: "))
g3 = float(input("Enter grade 3: "))
g4 = float(input("Enter grade 4: "))
g5 = float(input("Enter grade 5: "))

# Store in list
grades = [g1, g2, g3, g4, g5]

# Compute average
average = sum(grades) / 5

# Find letter grade
letter = get_letter_grade(average)

# Output
print()
print(name)
print("List:", *grades)
print(f"{name}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter}")
