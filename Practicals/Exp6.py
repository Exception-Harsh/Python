user = False
while not user:
    choice = int(input("Enter Choice: "))

    if choice == 1:
        l1 = [int(x) for x in input("Enter Key Values: ").split()]
        l2 = [x for x in input("Enter Values: ").split()]
        z1 = zip(l1, l2)
        d1 = dict(z1)

        l3 = [int(x) for x in input("Enter Dict 2 keys: ").split()]
        l4 = [x for x in input("Enter values for Dict 2: ").split()]
        z2 = zip(l3, l4)
        d2 = dict(z2)
        print(f"Dict 1: -{d1} \nDict 2: , {d2}")

    elif choice == 2:
        d1.update(d2)
        print(f"Concatenated Dictionary - {d1}")
        p = int(input("Delete the value of key: "))
        d1.pop(p)
        print(f"Updated Dict - {d1}")

    elif choice == 3:
        l3 = d1.keys()
        s1 = int(input("Enter the key to be searched: "))
        for x in l3:
            if s1 == x:
                print("Value at key {} is {}".format(s1, d1[s1]))

    elif choice == 4:
        l5 = [int(x) for x in input("Enter Zip Code: ").split()]
        l6 = [x for x in input("Enter city names: ").split()]
        z3 = zip(l5, l6)
        d3 = dict(z3)
        print(f"Mapped Dictionary {d3}")

    elif choice == 5:
        user = True

    else:
        print("Invalid Choice")
