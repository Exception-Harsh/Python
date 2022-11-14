import sys

a = (sys.argv[0])
b = (sys.argv[1])

print("Before Swapping")
print(a, b)

print("After Swapping: ")
temp = a
a = b
b = temp
print('a: ' + a, 'b: ' + b)

a = int(a)
if a > 0:
    print("a is a positive number")
elif a < 0:
    print("a is a negative number")
else:
    print("a is zero")
