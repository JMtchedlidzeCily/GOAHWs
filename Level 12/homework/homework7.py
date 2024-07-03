score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
elif score < 60:
    print("Grade F")
else:
    print("Invalid score entered. Please enter a score between 0 and 100.")
