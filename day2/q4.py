numbers = list(map(int, input("Enter numbers separated by space: ").split()))
smallest = min(numbers)
print("The smallest number is:", smallest)


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
new = list(set(numbers))
new.sort(reverse=True)
if len(new) >= 2:
    print("The second greatest number is:", new[1])
else:
    print("Not enough unique numbers to find second greatest.")


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
new = list(set(numbers))
new.sort()

if len(new) >= 2:
    print("The second smallest number is:", new[1])
else:
    print("Not enough unique numbers to find second smallest.")
