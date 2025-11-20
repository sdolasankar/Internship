# Simple Student Grade Calculator
# Works in Python 3.x. Copy/paste into Google Colab, Replit, or a local .py file.

def get_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            num = float(val)
            if num < 0 or num > 100:
                print("Please enter a number between 0 and 100.")
                continue
            return num
        except ValueError:
            print("That's not a valid number. Try again.")

def percent_to_grade(pct):
    # Grade boundaries - edit to match your teacher's rubric if needed
    if pct >= 90:
        return "A+", "Outstanding work! Keep it up!"
    if pct >= 80:
        return "A", "Very good! You're doing great."
    if pct >= 70:
        return "B", "Good job! A little more practice and you'll be even better."
    if pct >= 60:
        return "C", "Satisfactory — keep practicing."
    if pct >= 50:
        return "D", "You're getting there — try reviewing the topics you find hard."
    return "F", "Don't be discouraged — ask for help and try again!"

def grade_single_student():
    print("\n--- Student Grade Calculator (single student) ---")
    name = input("Enter student's name: ").strip()
    num_subjects = 0
    while True:
        try:
            num_subjects = int(input("How many subjects? ").strip())
            if num_subjects <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Enter a whole number (e.g., 5).")

    marks = []
    for i in range(1, num_subjects + 1):
        m = get_float(f"Enter marks for subject {i} (0-100): ")
        marks.append(m)

    total = sum(marks)
    percentage = total / num_subjects
    grade, message = percent_to_grade(percentage)

    print("\n--- Result ---")
    print(f"Name      : {name}")
    print(f"Total     : {total:.2f} / {100 * num_subjects:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade     : {grade}")
    print(f"Note      : {message}")
    print("----------------\n")

def grade_multiple_students():
    print("\n--- Student Grade Calculator (multiple students) ---")
    while True:
        grade_single_student()
        again = input("Do you want to grade another student? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

def main():
    print("Simple Student Grade Calculator")
    print("1. Single student")
    print("2. Multiple students (repeat)")
    choice = input("Choose mode (1 or 2): ").strip()
    if choice == "2":
        grade_multiple_students()
    else:
        grade_single_student()

if __name__ == "__main__":
    main()
