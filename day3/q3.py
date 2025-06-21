s = input("Enter the string: ")
length = len(s)
mid = length // 2

rev = -1
for a in range(mid):
    if s[a] == s[rev]:
        rev -= 1
    else:
        print(s, "is not a palindrome")
        break
else:
    print(s, "is a palindrome")
