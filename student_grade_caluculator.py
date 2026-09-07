# Student Grade Calculator
# This program calculates total marks, average, grade, and pass/fail result.

# Get the number of subjects
n = int(input("Enter number of subjects: "))

total = 0

# Get marks for each subject
for i in range(1, n + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

# Calculate average
average = total / n

# Assign grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"

# Check pass or fail
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display the result
print("\n----- Student Grade Report -----")
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
print("Result:", result)
