h = int(input("Enter h: "))
n = int(input("Enter n: "))

for u in range(n):
    d = int(input("Enter Damage: "))
    h = h-d

if h > 0:
    print("True")
else:
    print("False")


