
name = input("Enter student name: ")
student_class = input("Enter class: ")
print("Enter marks for 5 subjects:")
mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))
mark4 = float(input("Subject 4: "))
mark5 = float(input("Subject 5: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100

if percentage >= 60:
    print("grade A")
elif percentage >=50 and percentage<60:
    print("grade B")
elif percentage >= 40 and percentage < 50:
    print("print c")
elif percentage >= 33 and percentage < 40:
    print("grade d")
else:
    print("better luck next time")