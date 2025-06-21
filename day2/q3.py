a = []
n = int(input("Enter how many times you want to use the billing system: "))
for _ in range(n):
    print("1. Create Bill")
    print("2. Display Items and Total")
    print("3. Display Total Only")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        item = input("Enter item name: ")
        price = input("Enter item price: ")
        a.append([item, price])
        print("Item added.\n")
    else:
        if choice == '2':
            if not a:
                print("No items in the bill.\n")
            else:
                total = 0
                print("\nItems in the Bill:")
                for i in a:
                    print(i[0], ": $", i[1])
                    total = total + float(i[1])
                print("Total Bill Amount: $", total, "\n")
        else:
            if choice == '3':
                total = 0
                for i in a:
                    total = total + float(i[1])
                print("Total Amount: $", total, "\n")
            else:
                if choice == '4':
                    print("Exiting program. Thank you!")
                    break
                else:
                    print("Invalichoice.\n")