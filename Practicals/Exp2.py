print("Menu Driven Program")
print("1. Accept Number")
print("2. Accept String")

choice = int(input("Enter your choice: "))

if choice == 1:
    num = int(input("Enter Number: "))
    fact = 1
    if num < 0:
        print("Negative Number doesn't have Factorial")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fact *= i
        print("Factorial of ", num, " is ", fact)

elif choice == 2:
    string = input("Enter String: ")
    if string == string[::-1]:
        print("The string is palindrome")
    else:
        print("It is not palindrome")

else:
    print("Wrong Choice")
