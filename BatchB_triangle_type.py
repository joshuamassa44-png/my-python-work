a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if (a==b):
    if b == c:
        print("Equilateral")
    else: 
        print("Isoceles")
elif (b==c):
    print("Isoceles")
elif (a==c):
    print("Isoceles")
else:
    print("Scalene")
