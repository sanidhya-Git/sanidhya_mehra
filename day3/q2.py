def maths(a=0, b=0):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division Cannot divide by zero")


a = int(input("enter the a value"))
b = int(input("enter the b value "))

maths(a, b)