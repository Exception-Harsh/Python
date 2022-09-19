list1 = [int(x) for x in input("Enter Odd Values: ").split()]
list2 = [int(x) for x in input("Enetr Even Values: ").split()]
print("Odd List: ", list1, "Even List: ", list2)
list3 = list()

x = 1
while x < 10:
    print("1: Print list \t 2: Sorted List \t 3: Replace 1st element \t 4: Remove mid element \t 5: Max & Min of list \t 6: Identifying python")
    choice = int(input("Enter Choice: "))
    list3 = list1 + list2

    if choice == 1:
        print(list3)

    elif choice == 2:
        list3.sort()
        print("Sorted List: ", list3)

    elif choice == 3:
        list3[0] = int(input("Enter the value to replace first element: "))
        print(list3)

    elif choice == 4:
        mid = len(list3)//2
        list3.remove(list3[mid])
        print("List 3: ", list3)

    elif choice == 5:
        print("Max of list: ", max(list3), "Min of list: ", min(list3))

    elif choice == 6:
        listn = [x for x in input("Enter Name: ").split()]
        for n in listn:
            list3.append(n)
        print("List 3: ", list3)
        try:
            if list3.index("py"):
                print("Python present")
        except ValueError:
            print("Python is absent")

    else:
        break
