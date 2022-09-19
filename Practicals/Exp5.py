s1 = {x for x in input("Enter String: ")}
s2 = {x for x in input("Enter String: ")}

print(s1, "::::", s2)
x = 1
while x < 10:
    print("1: Intersection  2: Difference  3: Union  4: Symmetric Difference  5: Exit ")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(s1.intersection(s2))

    elif choice == 2:
        print(s1.difference(s2))
    elif choice == 3:
        print(s1.union(s2))
    elif choice == 4:
        print(s1.symmetric_difference(s2))
    else:
        exit()
