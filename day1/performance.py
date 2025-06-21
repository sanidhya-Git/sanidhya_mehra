
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

if percentage >80:
    print("pass")
else:
    print("fail")
print("\n----- Student Result -----")
print("Name:", name)
print("Class:", student_class)
print("Total Marks:", total_marks)
print("Percentage: {:.2f}%".format(percentage))
print("percentage :")



print("--------------q2--------------")

a = str(input("Enter first string: "))
b = str(input("Enter second string: "))
c = a + b

print("\n----- String Operations -----")
print("Concatenated String:", c)
print("Uppercase:", c.upper())
print("Lowercase:", c.lower())
print("Title Case:", c.title())
print("Capitalized:", c.capitalize())
print("Length of String:", len(c))
print("Is Alphanumeric:", c.isalnum())
print("Is Alphabetic:", c.isalpha())
print("Reversed String:", c[::-1])
print("Count of 'a':", c.count('a'))
