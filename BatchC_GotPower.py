a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = 1
if a == b:
    print(n)
else:
    new_a = a
    while True:
        new_a = new_a*a
        n += 1
        if new_a == b:
            break
    print(n)

    