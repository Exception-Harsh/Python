class emp:
    def __init__(self, id1, name1):
        self.id = id1
        self.name = name1

    def display(self):
        print(self.id)
        print(self.name)

    def setvalue(self, id1, name1):
        self.id = id1
        self.name = name1


lst1 = list()
n = int(input("Enter Number of Employee: "))

for i in range(n):
    z = int(input("Enter Employee ID: "))
    a = input("Enter Name of Employee: ")
    e1 = emp(z, a)
    lst1.append(e1)

while 1:
    print("1: Print \t2: Change ID  \t3: Change Name \t5: exit ")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        for i in lst1:
            print("ID: ", i.id, "\nName: ", i.name)
    elif choice == 2:
        q = input("Enter Name of the employee to be changed: ")
        nid = int(input("Enter new ID: "))
        for d in lst1:
            if q == d.name:
                d.setvalue(nid, q)
        print("After Change: ")
        for i in lst1:
            print("ID: ", i.id, "Name: ", i.name)
    elif choice == 3:
        x = int(intput("Enter ID of employee who needs to be removed: "))
        for f in lst1:
            if f.id == x:
                lst1.remove(f)
            print("After Change: ")
            for i in lst1:
                print("ID: ", i.id, "Name: ", i.name)
    elif choice == 4:
        exit()
