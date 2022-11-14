num = int(input("Enter the number of students: "))
list1 = list()

for i in range(0, num):
    r = int(input("Enter roll number: "))
    name = input("Enter Name: ")
    m1 = int(input("Enter Marks 1: "))
    m2 = int(input("Enter Marks 2: "))
    m3 = int(input("Enter Marks 3: "))
    l1 = [r, name, m1, m2, m3]
    tp1 = tuple(l1)
    list1.append(tp1)

tp1 = tuple(list1)

print("Menu Driven Program")
print("1. All Elements\n2. Element with python\n3. Sorted Tuple\n4. Exit")
user = False

while not user:

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(tp1)

    elif choice == 2:
        for t in tp1:
            if "python" in t:
                print(t)

    elif choice == 3:
        print("Sorted Tuple according to names: ")
        print(sorted(tp1, key=lambda x: x[1]))

    elif choice == 4:
        print("Exited")
        break

else:
    print("Enter a valid choice.")
