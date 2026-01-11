T = int(input("Test cases: "))

for t in range(T):
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    count = 0
    for x in range(a,b+1):
        if ((x%c == 0) and (x%d != 0)):
            count += 1
    print(count)




